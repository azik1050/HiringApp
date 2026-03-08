from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.user_schemas import (
    CreateUserRequest,
    CreateUserResponse,
    GetUsersResponse,
    GetUserResponse
)
from src.app.services.user_service import UserService
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/users", tags=["User Controller"])
service = UserService()


@router.get('/{user_id}/', status_code=200, response_model=GetUserResponse)
async def get_user(
        user_id: int,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.get_user(user_id=user_id, db=db)


@router.get('/', status_code=200, response_model=GetUsersResponse)
async def get_users(
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.get_users(db=db)


@router.post('/', status_code=201, response_model=CreateUserResponse)
async def create_user(
        user: CreateUserRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_user(user=user, db=db)


@router.delete('/{user_id}/', status_code=204, response_model={})
async def delete_user(
        user_id: int,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.delete_user(id=user_id, db=db)
