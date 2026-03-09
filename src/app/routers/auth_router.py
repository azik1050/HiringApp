from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.auth_schemas import (
    LoginRequest,
    LoginResponse
)
from src.app.services.auth_service import AuthService
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/auth", tags=["Auth Controller"])
service = AuthService()


@router.post('/login', status_code=200, response_model=LoginResponse)
async def login(
        creds: LoginRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.login(creds=creds, db=db)
