"""Control dependency graph API — Task 3.10.

GET /api/v1/graph

Returns nodes (control groups + ISO controls + mapped external controls) and
edges (cross-framework mappings + group-to-control containment) suitable for
Cytoscape.js or any graph visualisation library.

Query parameters:
  center      — group_code to centre on (partial match); omit for full graph
  depth       — edge traversal depth (1-3, default 2)
  edge_types  — comma-separated mapping types to include (default: all)
  section     — filter to one ISO 27001 section (A.5 | A.6 | A.7 | A.8)
  max_nodes   — cap on returned nodes (default 300, max 500)
"""

import logging

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.users import User
from src.schemas.dashboard import GraphResponse
from src.services import dashboard_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/graph", tags=["graph"])


@router.get("", response_model=GraphResponse)
def get_graph(
    source_framework: str = Query("ISO27001", description="Source framework code prefix (ISO27001 | ISO27701 | ISO27017)"),
    center: str | None = Query(None, description="Control group code (partial match) to centre on"),
    depth: int = Query(2, ge=1, le=3, description="Traversal depth (1=groups only, 2=+ISO controls, 3=+mappings)"),
    edge_types: str | None = Query(None, description="Comma-separated mapping types (maps-to, mitigates, detects, …)"),
    section: str | None = Query(None, description="Filter to section (ISO27001: A.5/A.6/A.7/A.8 | ISO27701: A.1/A.2/A.3)"),
    max_nodes: int = Query(300, ge=10, le=500),
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Control dependency graph with cross-framework mapping edges."""
    edge_type_list = [e.strip() for e in edge_types.split(",")] if edge_types else None
    return dashboard_service.get_graph(
        db,
        source_framework=source_framework,
        center=center,
        depth=depth,
        edge_types=edge_type_list,
        section=section,
        max_nodes=max_nodes,
    )
