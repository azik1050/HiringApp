from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models import CandidateAccountModel, CompanyAccountModel
from src.app.models.user_model import UserModel
from src.app.schemas.user_schemas import CreateUserRequest
from sqlalchemy import delete, select, Row, MappingResult


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
    async def get_user_by_name(
            name: str,
            db: AsyncSession
    ) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(UserModel.name == name)
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
            name=user.name,
            password=user.password
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

    @staticmethod
    async def get_full_user_info(
            id: int,
            db: AsyncSession
    ) -> Optional[MappingResult]:
        query = (
            select(
                UserModel.id,
                UserModel.name,
                CandidateAccountModel.id.label("candidate_account_id"),
                CompanyAccountModel.id.label("company_account_id")
            )
            .where(UserModel.id == id)
            .outerjoin(CandidateAccountModel, CandidateAccountModel.user_id == UserModel.id)
            .outerjoin(CompanyAccountModel, CompanyAccountModel.owner_id == UserModel.id)
        )

        result = await db.execute(query)

        return result.mappings().one_or_none()

