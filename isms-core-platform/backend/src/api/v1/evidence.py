"""Evidence upload and management endpoints.

POST   /api/v1/evidence/upload              — upload a single file, create evidence record
POST   /api/v1/evidence/bulk-draft          — upload multiple files as drafts (no control group)
GET    /api/v1/evidence/                    — list evidence (filters: control, type, status)
GET    /api/v1/evidence/{id}               — detail
GET    /api/v1/evidence/{id}/download      — stream the file
PATCH  /api/v1/evidence/{id}               — update metadata
PATCH  /api/v1/evidence/{id}/assign        — assign draft to control group
PATCH  /api/v1/evidence/{id}/submit        — submit for approval (draft/active → pending_review)
PATCH  /api/v1/evidence/{id}/approve       — approve (admin/isms_manager only)
PATCH  /api/v1/evidence/{id}/reject        — reject (admin/isms_manager only)
DELETE /api/v1/evidence/{id}               — delete record + file

Supported file types: .docx .pdf .xlsx .png .jpg .jpeg .txt .md .csv .json
Max file size: 50 MB
"""

import csv
import io
import mimetypes
import uuid
from datetime import date, datetime, timezone

from fastapi import APIRouter, Depends, File, Form, HTTPException, Query, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user, require_admin
from src.database.enums import EvidenceStatus, UserRole
from src.database.session import get_db
from src.domain.users import User
from src.schemas.evidence import EvidenceAssign, EvidenceRead, EvidenceReview, EvidenceUpdate
from src.services import evidence_service
from src.services.control_service import get_control_group, get_control_group_by_code

router = APIRouter(prefix="/evidence", tags=["evidence"])


@router.post("/upload", response_model=EvidenceRead, status_code=201)
async def upload_evidence(
    file: UploadFile = File(..., description="Evidence file (.docx, .pdf, .xlsx, .png, .jpg, .jpeg, .txt, .csv, .json)"),
    evidence_type: str = Form(..., description="Type: document|screenshot|log_extract|config_export|test_result|attestation"),
    title: str = Form(..., description="Descriptive title for this evidence item"),
    group_code: str | None = Form(None, description="Control group code (e.g. a.8.8). Use this or control_group_id."),
    control_group_id: uuid.UUID | None = Form(None, description="Control group UUID. Use this or group_code."),
    requirement_id: uuid.UUID | None = Form(None, description="Optional: link to specific requirement"),
    assessment_item_id: uuid.UUID | None = Form(None, description="Optional: link to specific assessment item"),
    collected_date: date | None = Form(None, description="Date evidence was collected (YYYY-MM-DD)"),
    expires_date: date | None = Form(None, description="Date evidence expires (YYYY-MM-DD)"),
    notes: str | None = Form(None, description="Free-text notes"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Upload an evidence file and create an evidence record assigned to a control group."""
    cg = None
    if group_code:
        cg = get_control_group_by_code(db, group_code)
    elif control_group_id:
        cg = get_control_group(db, control_group_id)

    if not cg:
        raise HTTPException(status_code=400, detail="Must provide a valid group_code or control_group_id")

    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    try:
        evidence_service.validate_extension(file.filename)
    except ValueError as e:
        raise HTTPException(status_code=415, detail=str(e))

    file_bytes = await file.read()
    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    try:
        ev = evidence_service.create_evidence(
            db=db,
            control_group_id=cg.id,
            group_code=cg.group_code,
            file_bytes=file_bytes,
            original_filename=file.filename,
            evidence_type=evidence_type,
            title=title,
            requirement_id=requirement_id,
            assessment_item_id=assessment_item_id,
            collected_date=collected_date,
            expires_date=expires_date,
            notes=notes,
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    db.commit()
    db.refresh(ev)
    return ev


@router.post("/bulk-draft", response_model=list[EvidenceRead], status_code=201)
async def bulk_draft_upload(
    files: list[UploadFile] = File(..., description="One or more evidence files"),
    evidence_type: str = Form("document", description="Shared evidence type for all files"),
    notes: str | None = Form(None, description="Shared notes for all files"),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Bulk upload evidence files as drafts.

    Files are stored without a control group assignment.
    Use PATCH /evidence/{id}/assign to assign each draft to a control group.
    """
    if not files:
        raise HTTPException(status_code=400, detail="No files provided")
    if len(files) > 50:
        raise HTTPException(status_code=400, detail="Maximum 50 files per bulk upload")

    created = []
    errors = []

    for upload in files:
        if not upload.filename:
            errors.append("A file had no filename — skipped")
            continue
        try:
            evidence_service.validate_extension(upload.filename)
        except ValueError as e:
            errors.append(f"{upload.filename}: {e}")
            continue

        file_bytes = await upload.read()
        if not file_bytes:
            errors.append(f"{upload.filename}: empty file — skipped")
            continue

        title = upload.filename.rsplit(".", 1)[0].replace("_", " ").replace("-", " ")

        try:
            ev = evidence_service.create_draft_evidence(
                db=db,
                file_bytes=file_bytes,
                original_filename=upload.filename,
                evidence_type=evidence_type,
                title=title,
                notes=notes,
            )
            created.append(ev)
        except ValueError as e:
            errors.append(f"{upload.filename}: {e}")

    if errors:
        # Partial success: commit what worked, report errors in header
        import logging
        logging.getLogger(__name__).warning("Bulk upload partial errors: %s", errors)

    db.commit()
    for ev in created:
        db.refresh(ev)
    return created


@router.get("/", response_model=list[EvidenceRead])
def list_evidence(
    control_group_id: uuid.UUID | None = Query(None),
    group_code: str | None = Query(None, description="Filter by group code (e.g. a.8.8)"),
    evidence_type: str | None = Query(None, description="Filter by type"),
    evidence_status: str | None = Query(None, description="Filter by status: draft|pending_review|approved|rejected|active"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """List evidence items with optional filters."""
    cg_id = control_group_id
    if group_code and not cg_id:
        cg = get_control_group_by_code(db, group_code)
        if cg:
            cg_id = cg.id

    return evidence_service.list_evidence(
        db,
        control_group_id=cg_id,
        evidence_type=evidence_type,
        evidence_status=evidence_status,
        limit=limit,
        offset=offset,
    )


@router.get("/export")
def export_evidence(
    group_code: str | None = Query(None),
    evidence_type: str | None = Query(None),
    evidence_status: str | None = Query(None),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Export manual evidence as CSV."""
    cg_id = None
    if group_code:
        cg = get_control_group_by_code(db, group_code)
        if cg:
            cg_id = cg.id
    items = evidence_service.list_evidence(
        db,
        control_group_id=cg_id,
        evidence_type=evidence_type,
        evidence_status=evidence_status,
        limit=10000,
        offset=0,
    )
    cols = ["id", "title", "evidence_type", "evidence_status", "collected_date", "expires_date", "created_at"]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore")
    w.writeheader()
    for item in items:
        w.writerow({
            "id": str(item.id),
            "title": item.title or "",
            "evidence_type": item.evidence_type.value if item.evidence_type else "",
            "evidence_status": item.evidence_status.value if item.evidence_status else "",
            "collected_date": item.collected_date.isoformat() if item.collected_date else "",
            "expires_date": item.expires_date.isoformat() if item.expires_date else "",
            "created_at": item.created_at.isoformat() if item.created_at else "",
        })
    buf.seek(0)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"manual_evidence_{group_code or 'all'}_{ts}.csv"
    return StreamingResponse(
        iter([buf.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@router.get("/{evidence_id}", response_model=EvidenceRead)
def get_evidence(
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Get evidence detail by ID."""
    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")
    return ev


@router.get("/{evidence_id}/download")
def download_evidence(
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Stream the evidence file as a download."""
    from pathlib import Path

    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    file_path = Path(ev.file_path)
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Evidence file not found on disk")

    media_type, _ = mimetypes.guess_type(str(file_path))
    original_filename = ev.metadata_.get("original_filename", file_path.name)

    return FileResponse(
        path=str(file_path),
        media_type=media_type or "application/octet-stream",
        filename=original_filename,
    )


@router.patch("/{evidence_id}", response_model=EvidenceRead)
def update_evidence(
    evidence_id: uuid.UUID,
    updates: EvidenceUpdate,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Update evidence metadata (title, dates, verification, notes)."""
    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    ev = evidence_service.update_evidence(db, ev, updates.model_dump(exclude_none=True))
    db.commit()
    db.refresh(ev)
    return ev


@router.patch("/{evidence_id}/assign", response_model=EvidenceRead)
def assign_evidence(
    evidence_id: uuid.UUID,
    body: EvidenceAssign,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Assign a draft evidence item to a control group.

    Set require_approval=true to move to pending_review; otherwise moves to active.
    """
    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    if ev.evidence_status not in (EvidenceStatus.DRAFT, EvidenceStatus.REJECTED):
        raise HTTPException(
            status_code=409,
            detail=f"Cannot assign evidence with status '{ev.evidence_status.value}'"
        )

    cg = None
    if body.group_code:
        cg = get_control_group_by_code(db, body.group_code)
    elif body.control_group_id:
        cg = get_control_group(db, body.control_group_id)

    if not cg:
        raise HTTPException(status_code=400, detail="Must provide a valid group_code or control_group_id")

    ev.control_group_id = cg.id
    ev.evidence_status = EvidenceStatus.PENDING_REVIEW if body.require_approval else EvidenceStatus.ACTIVE
    db.commit()
    db.refresh(ev)
    return ev


@router.patch("/{evidence_id}/submit", response_model=EvidenceRead)
def submit_evidence(
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Submit an evidence item for manager approval (active → pending_review)."""
    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    if ev.evidence_status not in (EvidenceStatus.ACTIVE, EvidenceStatus.REJECTED):
        raise HTTPException(
            status_code=409,
            detail=f"Cannot submit evidence with status '{ev.evidence_status.value}'"
        )
    if not ev.control_group_id:
        raise HTTPException(status_code=409, detail="Assign evidence to a control group before submitting for review")

    ev.evidence_status = EvidenceStatus.PENDING_REVIEW
    db.commit()
    db.refresh(ev)
    return ev


@router.patch("/{evidence_id}/approve", response_model=EvidenceRead)
def approve_evidence(
    evidence_id: uuid.UUID,
    body: EvidenceReview,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Approve a pending evidence item. Requires admin or isms_manager role."""
    if _user.role not in (UserRole.ADMIN, UserRole.ISMS_MANAGER):
        raise HTTPException(status_code=403, detail="Only admin or isms_manager can approve evidence")

    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    if ev.evidence_status != EvidenceStatus.PENDING_REVIEW:
        raise HTTPException(
            status_code=409,
            detail=f"Cannot approve evidence with status '{ev.evidence_status.value}'"
        )

    ev.evidence_status = EvidenceStatus.APPROVED
    ev.verified_by = _user.full_name or _user.email
    from datetime import date
    ev.verified_date = date.today()
    if body.reason:
        meta = dict(ev.metadata_)
        meta["approval_note"] = body.reason
        ev.metadata_ = meta

    db.commit()
    db.refresh(ev)
    return ev


@router.patch("/{evidence_id}/reject", response_model=EvidenceRead)
def reject_evidence(
    evidence_id: uuid.UUID,
    body: EvidenceReview,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Reject a pending evidence item. Requires admin or isms_manager role."""
    if _user.role not in (UserRole.ADMIN, UserRole.ISMS_MANAGER):
        raise HTTPException(status_code=403, detail="Only admin or isms_manager can reject evidence")

    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    if ev.evidence_status != EvidenceStatus.PENDING_REVIEW:
        raise HTTPException(
            status_code=409,
            detail=f"Cannot reject evidence with status '{ev.evidence_status.value}'"
        )

    ev.evidence_status = EvidenceStatus.REJECTED
    if body.reason:
        meta = dict(ev.metadata_)
        meta["rejection_reason"] = body.reason
        ev.metadata_ = meta

    db.commit()
    db.refresh(ev)
    return ev


@router.delete("/{evidence_id}", status_code=204)
def delete_evidence(
    evidence_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Delete evidence record and its uploaded file."""
    ev = evidence_service.get_evidence(db, evidence_id)
    if not ev:
        raise HTTPException(status_code=404, detail="Evidence not found")

    evidence_service.delete_evidence(db, ev)
    db.commit()
