from fastapi.routing import APIRouter

from auth_service.web.api import echo, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
