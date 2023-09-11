from fastapi import APIRouter
from controllers.task_controller import router as task_router
from controllers.ml_controller import router as ml_router

router = APIRouter()

# router.include_router(task_router)
router.include_router(ml_router)