from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.create_user_schemas import (
    CreateUserRequest,
    GetUsersResponse,
    User,
    CreateUserResponse,
    GetUserResponse
)


class UserService:
    def __init__(self, user_repo: UserRepository):
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

        return GetUserResponse(**user)

    async def get_users(
            self
    ) -> GetUsersResponse:
        users = await self.user_repo.get_users()

        return GetUsersResponse(
            data=[
                User(
                    id=user.id,
                    name=user.name
                )
                for user in users
            ]
        )

    async def create_user(
            self,
            user: CreateUserRequest
    ) -> CreateUserResponse:
        try:
            created_user = await self.user_repo.create_user(user)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already exists")
        return CreateUserResponse(id=created_user.id, name=created_user.name)

    async def delete_user(
            self,
            id: int
    ) -> dict:
        await self.user_repo.delete_user(id)
        return {}
