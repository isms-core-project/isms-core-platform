import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as DBSession

from src.core.dependencies import get_current_user
from src.database.session import get_db
from src.domain.content import Implementation
from src.domain.users import User

router = APIRouter(prefix="/implementations", tags=["implementations"])


@router.get("/{impl_id}/content")
def get_implementation_content(
    impl_id: uuid.UUID,
    db: DBSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    impl = db.get(Implementation, impl_id)
    if not impl:
        raise HTTPException(status_code=404, detail="Implementation not found")
    path = Path(impl.file_path)
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found on filesystem")
    return {
        "document_id": impl.document_id,
        "title": impl.title,
        "impl_type": impl.impl_type.value if hasattr(impl.impl_type, "value") else str(impl.impl_type),
        "content": path.read_text(encoding="utf-8"),
    }
