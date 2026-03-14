from fastapi import APIRouter

from src.api.v1 import ai, admin, assessments, auth, compass, connectors, controls, dashboard, evidence, frameworks, gaps, generators, graph, health, implementations, organisation, policies, qa, search, sync

api_router = APIRouter()

# Health (no prefix, no auth)
api_router.include_router(health.router)

# V1 API routes
api_router.include_router(auth.router, prefix="/api/v1")
api_router.include_router(controls.router, prefix="/api/v1")
api_router.include_router(frameworks.router, prefix="/api/v1")
api_router.include_router(assessments.router, prefix="/api/v1")
api_router.include_router(admin.router, prefix="/api/v1")
api_router.include_router(search.router, prefix="/api/v1")
api_router.include_router(sync.router, prefix="/api/v1")
api_router.include_router(dashboard.router, prefix="/api/v1")
api_router.include_router(graph.router, prefix="/api/v1")
api_router.include_router(evidence.router, prefix="/api/v1")
api_router.include_router(gaps.router, prefix="/api/v1")
api_router.include_router(policies.router, prefix="/api/v1")
api_router.include_router(implementations.router, prefix="/api/v1")
api_router.include_router(ai.router, prefix="/api/v1")
api_router.include_router(compass.router, prefix="/api/v1")
api_router.include_router(qa.router, prefix="/api/v1")
api_router.include_router(generators.router, prefix="/api/v1")
api_router.include_router(organisation.router, prefix="/api/v1")
api_router.include_router(connectors.router, prefix="/api/v1")
