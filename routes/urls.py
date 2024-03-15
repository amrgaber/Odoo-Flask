from fastapi import APIRouter
from .root import router as employee_router

router = APIRouter()

router.include_router(employee_router, tags=["Home"])
