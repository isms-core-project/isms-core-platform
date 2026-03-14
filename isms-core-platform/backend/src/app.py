"""FastAPI application factory."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.api.router import api_router
from src.core.config import get_settings
from src.core.exceptions import generic_exception_handler, http_exception_handler
from src.core.security import hash_password
from src.database.session import SessionLocal
from src.services import search_service
from src.services.loader_service import load_all_bundles, needs_seed
from src.services.qa_service import ensure_synonym_table

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: auto-seed frameworks on first boot."""
    settings = get_settings()
    logger.info("ISMS CORE API starting (debug=%s)", settings.debug)

    db = SessionLocal()
    try:
        if needs_seed(db):
            logger.info("First boot detected — loading dataset bundles…")
            stats = load_all_bundles(db)
            logger.info("Seed complete: %s", stats)
        else:
            logger.info("Frameworks already loaded — skipping seed")
    except Exception as e:
        logger.error("Seed failed: %s", e)
    finally:
        db.close()

    # QA: ensure synonym_rules table exists and is seeded
    try:
        ensure_synonym_table()
        logger.info("Synonym rules table ready")
    except Exception as e:
        logger.error("Synonym table setup failed: %s", e)

    # OpenSearch: verify connectivity and ensure indices
    try:
        if search_service.is_available():
            search_service.ensure_indices()
            logger.info("OpenSearch connected — indices ensured")
        else:
            logger.warning(
                "OpenSearch not available — search disabled (non-fatal)"
            )
    except Exception as e:
        logger.warning("OpenSearch init failed: %s (non-fatal)", e)

    # Seed/update admin user from ADMIN_EMAIL / ADMIN_PASSWORD env vars
    if settings.admin_email and settings.admin_password:
        try:
            from src.domain.users import User
            from sqlalchemy import select
            db2 = SessionLocal()
            try:
                user = db2.execute(
                    select(User).where(User.email == settings.admin_email)
                ).scalar_one_or_none()
                hashed = hash_password(settings.admin_password)
                if user:
                    user.hashed_password = hashed
                    logger.info("Admin password updated from env (email=%s)", settings.admin_email)
                else:
                    db2.add(User(
                        email=settings.admin_email,
                        username="admin",
                        hashed_password=hashed,
                        full_name="Administrator",
                        role="admin",
                        is_active=True,
                    ))
                    logger.info("Admin user created from env (email=%s)", settings.admin_email)
                db2.commit()
            finally:
                db2.close()
        except Exception as e:
            logger.error("Admin seeding failed: %s", e)

    yield  # App is running

    logger.info("ISMS CORE API shutting down")


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title="ISMS CORE Platform API",
        description="ISO 27001:2022 ISMS compliance management platform",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # CORS
    origins = [o.strip() for o in settings.cors_origins.split(",")]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type", "Accept"],
        expose_headers=["X-QA-Status", "X-QA-Issues"],
    )

    # Exception handlers
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)

    # Routes
    app.include_router(api_router)

    return app
