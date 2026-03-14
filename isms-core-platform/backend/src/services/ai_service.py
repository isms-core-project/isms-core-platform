"""AI assistant service — BYOK Anthropic integration.

Builds ISMS-aware context from the DB and streams Claude responses via SSE.
Model is configurable via settings (default: claude-haiku-4-5-20251001).
"""

import json
import logging
import uuid
from typing import AsyncGenerator

from sqlalchemy import select
from sqlalchemy.orm import Session as DBSession

from src.core.config import get_settings
from src.domain.assessments import Assessment
from src.domain.compliance import Gap
from src.domain.content import Implementation, Policy
from src.domain.control_groups import ControlGroup

logger = logging.getLogger(__name__)

SYSTEM_BASE = """You are an expert ISO 27001:2022 ISMS consultant and auditor embedded in ISMS CORE, a professional GRC platform.

Your role:
- Answer questions about control groups, their current compliance state, and ISO 27001:2022 requirements
- Suggest evidence to collect for audit readiness
- Help interpret compliance scores and gaps
- Draft remediation plans for open gaps
- Review policy and implementation coverage
- Prepare users for audit questions

Be concise, practical, and direct. Use British English spelling. Reference specific items from the context when relevant. Do not pad responses with generic disclaimers."""

SYSTEM_CONTROL = SYSTEM_BASE + """

=== CONTROL GROUP STATE ===
{context}"""

SYSTEM_AUDIT_PREP = SYSTEM_BASE + """
You are now acting as a strict ISO 27001:2022 Lead Auditor conducting a Stage 2 audit. Ask probing questions about the control, challenge the evidence, and identify weaknesses as a real auditor would.

=== CONTROL GROUP STATE ===
{context}"""

SYSTEM_GAP_NARRATOR = SYSTEM_BASE + """
You are drafting an executive-level gap analysis narrative for this control group. Write in clear, board-ready language. Be specific about the gaps, their risk implications, and recommended remediation timelines.

=== CONTROL GROUP STATE ===
{context}"""


def _build_control_context(db: DBSession, control_id: str) -> str:
    """Build a structured text summary of a control group for AI context injection."""
    try:
        cg_id = uuid.UUID(control_id)
    except ValueError:
        return "Invalid control ID."

    cg = db.get(ControlGroup, cg_id)
    if not cg:
        return "Control group not found."

    lines = [
        f"Control Group: {cg.group_code.upper()} — {cg.name}",
        f"Section: {cg.section} ({cg.section_name})",
        f"Framework Status: {cg.framework_status} | Operational Status: {cg.operational_status}",
        f"Has Framework Product: {'Yes' if cg.has_framework else 'No'} | Has Operational Product: {'Yes' if cg.has_operational else 'No'}",
        "",
    ]

    # Policies
    policies = db.execute(
        select(Policy).where(Policy.control_group_id == cg_id).order_by(Policy.document_id)
    ).scalars().all()
    if policies:
        lines.append(f"POLICIES ({len(policies)}):")
        for p in policies:
            lines.append(f"  [{p.policy_type}] {p.document_id}: {p.title} ({p.word_count or 0} words)")
        lines.append("")

    # Implementations
    impls = db.execute(
        select(Implementation).where(Implementation.control_group_id == cg_id).order_by(Implementation.document_id)
    ).scalars().all()
    if impls:
        lines.append(f"IMPLEMENTATION GUIDES ({len(impls)}):")
        for i in impls:
            lines.append(f"  [{i.impl_type}] {i.document_id}: {i.title} ({i.word_count or 0} words)")
        lines.append("")

    # Assessments
    assessments = db.execute(
        select(Assessment).where(Assessment.control_group_id == cg_id).order_by(Assessment.document_id)
    ).scalars().all()
    if assessments:
        lines.append(f"ASSESSMENTS ({len(assessments)}):")
        for a in assessments:
            score = f"{float(a.overall_score):.0f}%" if a.overall_score else "not scored"
            lines.append(f"  [{a.assessment_type.upper()}] {a.document_id}: {a.workbook_name} — {score}")
            if a.items_total:
                lines.append(
                    f"    {a.items_total} items: {a.items_compliant} compliant, "
                    f"{a.items_partial} partial, {a.items_non_compliant} non-compliant, "
                    f"{a.items_na} N/A"
                )
        lines.append("")

    # Open gaps
    gaps = db.execute(
        select(Gap)
        .where(Gap.control_group_id == cg_id, Gap.status != "closed")
        .order_by(Gap.severity)
    ).scalars().all()
    if gaps:
        lines.append(f"OPEN GAPS ({len(gaps)}):")
        for g in gaps:
            owner = f" — Owner: {g.owner}" if g.owner else ""
            lines.append(f"  [{g.severity.upper()}] {g.gap_description}{owner}")
        lines.append("")
    else:
        lines.append("OPEN GAPS: None")
        lines.append("")

    return "\n".join(lines)


def _build_system_prompt(db: DBSession, context_type: str, context_id: str | None, mode: str) -> str:
    if context_type == "control" and context_id:
        context = _build_control_context(db, context_id)
        template = SYSTEM_AUDIT_PREP if mode == "audit_prep" else (
            SYSTEM_GAP_NARRATOR if mode == "gap_narrator" else SYSTEM_CONTROL
        )
        return template.format(context=context)
    return SYSTEM_BASE


async def stream_chat(
    db: DBSession,
    messages: list[dict],
    context_type: str,
    context_id: str | None,
    mode: str,
) -> AsyncGenerator[str, None]:
    """Stream Claude response as SSE chunks."""
    import anthropic

    settings = get_settings()
    api_key = settings.anthropic_api_key

    if not api_key:
        yield f"data: {json.dumps({'error': 'ANTHROPIC_API_KEY not configured. Add it to your .env file.'})}\n\n"
        yield "data: [DONE]\n\n"
        return

    system = _build_system_prompt(db, context_type, context_id, mode)

    client = anthropic.AsyncAnthropic(api_key=api_key)
    try:
        async with client.messages.stream(
            model=settings.ai_model,
            max_tokens=2048,
            system=system,
            messages=messages,
        ) as stream:
            async for text in stream.text_stream:
                yield f"data: {json.dumps({'text': text})}\n\n"
    except anthropic.AuthenticationError:
        yield f"data: {json.dumps({'error': 'Invalid API key. Check ANTHROPIC_API_KEY in settings.'})}\n\n"
    except anthropic.RateLimitError:
        yield f"data: {json.dumps({'error': 'Rate limit reached. Please wait a moment and try again.'})}\n\n"
    except Exception as e:
        logger.error("AI stream error: %s", e)
        yield f"data: {json.dumps({'error': f'AI error: {str(e)}'})}\n\n"

    yield "data: [DONE]\n\n"
