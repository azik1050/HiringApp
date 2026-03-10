from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
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
        user = await UserRepository.get_full_user_info(
            id=user_id,
            db=db
        )

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return GetUserResponse(**user)
        # return GetUserResponse(
        #     id=user.id,
        #     name=user.name,
        #     candidate_account_id=user.candidate_account_id,
        #     company_account_id=user.company_account_id
        # )

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
        try:
            created_user = await UserRepository.create_user(user, db)
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already exists")
        return CreateUserResponse(id=created_user.id, name=created_user.name)

    async def delete_user(
            self,
            id: int,
            db: AsyncSession
    ) -> dict:
        await UserRepository.delete_user(id, db)
        return {}
