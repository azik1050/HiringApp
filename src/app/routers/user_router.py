from authx import TokenPayload
from fastapi import APIRouter, Depends
from src.app.dependencies.services import build_user_service
from src.app.schemas.create_user_schemas import (
    CreateUserRequest,
    CreateUserResponse,
    GetUsersResponse,
    GetUserResponse
)
from src.app.services.user_service import UserService
from src.core.auth.security import security

router = APIRouter(prefix="/users", tags=["User Controller"])


@router.get(
    '/info/',
    status_code=200,
    response_model=GetUserResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def get_user(
        token: TokenPayload = Depends(security.access_token_required),
        user_service: UserService = Depends(build_user_service)
):
    return await user_service.get_user(user_id=int(token.sub))


@router.get(
    '/',
    status_code=200,
    response_model=GetUsersResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def get_users(
        user_service: UserService = Depends(build_user_service)
):
    return await user_service.get_users()


@router.post(
    '/',
    status_code=201,
    response_model=CreateUserResponse,
    deprecated=True
)
async def create_user(
        user: CreateUserRequest,
        user_service: UserService = Depends(build_user_service)
):
    return await user_service.create_user(user=user)


@router.delete(
    '/{user_id}/',
    status_code=204,
    response_model={},
    deprecated=True
)
async def delete_user(
        user_id: int,
        user_service: UserService = Depends(build_user_service)
):
    return await user_service.delete_user(id=user_id)
