from fastapi import APIRouter

from app.api.routes.annotators import router as annotators_routers
from app.api.routes.distributions import router as distributions_router
from app.api.routes.skills import router as skills_router

router = APIRouter()

router.include_router(annotators_routers)
router.include_router(distributions_router)
router.include_router(skills_router)
