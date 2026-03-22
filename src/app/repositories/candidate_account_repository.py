from typing import Optional
from src.app.models import CandidateAccountModel
from sqlalchemy import select
from src.app.repositories._base_repository import BaseRepository


class CandidateAccountRepository(BaseRepository):
    async def get_candidate_account_id(
            self,
            user_id: int
    ) -> Optional[CandidateAccountModel.id]:
        query = (
            select(
                CandidateAccountModel.id.label("id")
            )
            .where(
                CandidateAccountModel.user_id == user_id
            )
        )

        result = await self._session.execute(query)

        return result.mappings().one_or_none()

    async def create_candidate_account(
            self,
            user_id: int
    ) -> CandidateAccountModel:
        candidate_account = CandidateAccountModel(
            user_id=user_id
        )

        return await self._add(candidate_account)

    async def get_candidate_account(
            self,
            user_id: int
    ) -> Optional[CandidateAccountModel]:
        query = (
            select(CandidateAccountModel)
            .where(CandidateAccountModel.user_id == user_id)
        )

        return await self._find_one(query)