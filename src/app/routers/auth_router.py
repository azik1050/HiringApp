from fastapi import APIRouter, Depends
from src.app.dependencies.services import build_auth_service
from src.app.schemas.auth_schemas import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse
)
from src.app.schemas.create_user_schemas import CreateUserRequest
from src.app.services.auth_service import AuthService


router = APIRouter(prefix="/auth", tags=["Auth Controller"])


@router.post(
    '/login',
    status_code=200,
    response_model=LoginResponse
)
async def login(
        creds: LoginRequest,
        auth_service: AuthService = Depends(build_auth_service)
):
    return await auth_service.login(creds=creds)


@router.post(
    '/register',
    status_code=200,
    response_model=RegisterResponse
)
async def register(
        user: RegisterRequest,
        auth_service: AuthService = Depends(build_auth_service)
):
    return await auth_service.register(user=user)
