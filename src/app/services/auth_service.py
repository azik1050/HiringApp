from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.auth.security import security
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.auth_schemas import (
    LoginResponse,
    LoginRequest
)


class AuthService:
    async def login(
            self,
            creds: LoginRequest,
            db: AsyncSession
    ) -> LoginResponse:
        existing_user = await UserRepository.get_user_by_name(
            name=creds.name,
            db=db
        )

        if not existing_user or existing_user.password != creds.password:
            raise HTTPException(
                status_code=401,
                detail="Invalid login or password"
            )
        else:
            token = security.create_access_token(
                uid=str(existing_user.id)
            )

            return LoginResponse(
                access_token=token
            )
