from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.user_schemas import CreateUserRequest, CreateUserResponse
from src.app.services.user_service import UserService
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/users", tags=["User Controller"])
service = UserService()


@router.post('/', status_code=201, response_model=CreateUserResponse)
async def create_user(
        user: CreateUserRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_user(user, db)
