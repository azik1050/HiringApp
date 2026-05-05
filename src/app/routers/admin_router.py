from fastapi import APIRouter, Depends

from src.app.dependencies.services import build_admin_service
from src.app.schemas.get_complaints_schemas import GetComplaintsResponse
from src.app.services.admin_service import AdminService

router = APIRouter(prefix="/admin", tags=["Admin Controller"])


@router.get(
    '/complaints/',
    status_code=200,
    response_model=GetComplaintsResponse,
    dependencies=[]
)
async def get_complaints(admin_service: AdminService = Depends(build_admin_service)):
    return await admin_service.show_complaints()
