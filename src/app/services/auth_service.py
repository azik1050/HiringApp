from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.services.mappers.auth_service_mapper import AuthServiceMapper
from src.core.auth.security import security
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.auth_schemas import (
    LoginResponse,
    LoginRequest,
    RegisterRequest
)


class AuthService:
    def __init__(
            self,
            user_repo: UserRepository
    ):
        self.mapper = AuthServiceMapper()
        self.user_repo = user_repo

    async def register(
            self,
            user: RegisterRequest
    ):
        try:
            created_user = await self.user_repo.create_user(
                user=user
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already exists")

        return self.mapper.user(created_user)

    async def login(
            self,
            creds: LoginRequest
    ) -> LoginResponse:
        existing_user = await self.user_repo.get_user_by_name(
            name=creds.name
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

            return self.mapper.auth_details(token)
