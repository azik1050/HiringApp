from typing import List, Optional
from src.app.models import CandidateAccountModel, CompanyAccountModel
from src.app.models.user_model import UserModel
from src.app.schemas.create_user_schemas import CreateUserRequest
from sqlalchemy import delete, select, MappingResult
from src.core.base_classes.repository import BaseRepository


class UserRepository(BaseRepository):
    """Class for interaction with users table"""
    async def get_user(
            self,
            user_id: int
    ) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(UserModel.id == user_id)
        )

        return await self._find_one(query)

    async def get_user_by_name(
            self,
            name: str
    ) -> Optional[UserModel]:
        query = (
            select(UserModel)
            .where(UserModel.name == name)
        )

        return await self._find_one(query)

    async def get_users(
            self
    ) -> List[UserModel]:
        query = (
            select(UserModel)
            .order_by(UserModel.id)
        )

        return await self._find_all(query)

    async def create_user(
            self,
            user: CreateUserRequest
    ) -> UserModel:
        user = UserModel(
            name=user.name,
            password=user.password
        )

        return await self._add(user)

    async def delete_user(
            self,
            id: int
    ) -> None:
        query = (
            delete(UserModel)
            .where(UserModel.id == id)
        )

        await self._session.execute(query)
        await self._session.commit()

    async def get_full_user_info(
            self,
            id: int
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

        return await self._find_one_labeled(query)

