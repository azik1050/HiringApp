from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.user_model import UserModel
from src.app.schemas.user_schemas import (
    CreateUserRequest,
    CreateUserResponse,
    GetUsersResponse,
    User
)
from sqlalchemy import delete, select


class UserRepository:
    @staticmethod
    async def get_user(
            user_id: int,
            db: AsyncSession
    ) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(UserModel.id == user_id)
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def get_users(
            db: AsyncSession
    ) -> List[UserModel]:
        query = (
            select(UserModel)
            .order_by(UserModel.id)
        )

        result = await db.execute(query)

        return [
            user for user in result.scalars().all()
        ]

    @staticmethod
    async def create_user(
            user: CreateUserRequest,
            db: AsyncSession
    ) -> UserModel:
        user = UserModel(
            name=user.name
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user

    @staticmethod
    async def delete_user(
            id: int,
            db: AsyncSession
    ) -> None:
        query = (
            delete(UserModel)
            .where(UserModel.id == id)
        )

        await db.execute(query)
        await db.commit()
