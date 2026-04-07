from fastapi import APIRouter

from src.api.v1 import ai, admin, assessments, auth, bia, collections, compass, connectors, controls, csrm, custom_frameworks, dashboard, ebios, evidence, feeds, frameworks, gaps, generators, glossary, graph, health, implementations, metrics, nist, organisation, policies, projects, qa, regulatory, risks, search, sync, vendors
from src.api.v1.remediation import acceptance_router, remediation_router
from src.api.v1 import coverage_inference

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
api_router.include_router(nist.router, prefix="/api/v1")
api_router.include_router(regulatory.router, prefix="/api/v1")
api_router.include_router(collections.router, prefix="/api/v1")
api_router.include_router(csrm.router, prefix="/api/v1")
api_router.include_router(projects.router, prefix="/api/v1")
api_router.include_router(risks.router, prefix="/api/v1")
api_router.include_router(acceptance_router, prefix="/api/v1")
api_router.include_router(remediation_router, prefix="/api/v1")
api_router.include_router(coverage_inference.router, prefix="/api/v1")
api_router.include_router(metrics.router, prefix="/api/v1")
api_router.include_router(vendors.router, prefix="/api/v1")
api_router.include_router(bia.router, prefix="/api/v1")
api_router.include_router(ebios.router, prefix="/api/v1")
api_router.include_router(custom_frameworks.router, prefix="/api/v1")
api_router.include_router(feeds.router, prefix="/api/v1")
api_router.include_router(glossary.router, prefix="/api/v1")
