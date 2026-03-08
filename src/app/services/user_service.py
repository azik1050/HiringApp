from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.user_schemas import (
    CreateUserRequest,
    GetUsersResponse,
    User,
    CreateUserResponse,
    GetUserResponse
)


class UserService:
    async def get_user(
            self,
            user_id: int,
            db: AsyncSession
    ) -> GetUserResponse:
        user = await UserRepository.get_user(
            user_id=user_id,
            db=db
        )

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        candidate_account_id = await CandidateAccountRepository.get_candidate_account(
            user_id=user_id,
            db=db
        )

        return GetUserResponse(
            id=user.id,
            name=user.name,
            candidate_account_id=candidate_account_id
        )

    async def get_users(
            self,
            db: AsyncSession
    ) -> GetUsersResponse:
        users = await UserRepository.get_users(db)
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
            user: CreateUserRequest,
            db: AsyncSession
    ) -> CreateUserResponse:
        created_user = await UserRepository.create_user(user, db)
        return CreateUserResponse(id=created_user.id, name=created_user.name)

    async def delete_user(
            self,
            id: int,
            db: AsyncSession
    ) -> dict:
        await UserRepository.delete_user(id, db)
        return {}
