from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.create_user_schemas import (
    CreateUserRequest,
    GetUsersResponse,
    CreateUserResponse,
    GetUserResponse
)
from src.app.services.mappers.user_service_mapper import UserServiceMapper


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.mapper = UserServiceMapper
        self.user_repo = user_repo

    async def get_user(
            self,
            user_id: int
    ) -> GetUserResponse:
        user = await self.user_repo.get_full_user_info(
            id=user_id
        )
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return self.mapper.user_info(user)

    async def get_users(
            self
    ) -> GetUsersResponse:
        users = await self.user_repo.get_users()

        return self.mapper.users_all(users)

    async def create_user(
            self,
            user: CreateUserRequest
    ) -> CreateUserResponse:
        try:
            created_user = await self.user_repo.create_user(user)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already exists")

        return self.mapper.created_user(created_user)

    async def delete_user(
            self,
            id: int
    ) -> dict:
        await self.user_repo.delete_user(id)
        return {}
