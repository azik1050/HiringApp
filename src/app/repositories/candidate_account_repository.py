from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models import CandidateAccountModel
from src.app.schemas.candidate_account_schemas import CreateCandidateAccountRequest
from sqlalchemy import select


class CandidateAccountRepository:
    @staticmethod
    async def get_candidate_account(
            user_id: int,
            db: AsyncSession
    ) -> Optional[CandidateAccountModel.id]:
        query = (
            select(CandidateAccountModel.id)
            .where(CandidateAccountModel.user_id == user_id)
        )

        result = await db.execute(query)

        return result.scalar_one_or_none()

    @staticmethod
    async def create_candidate_account(
            candidate: CreateCandidateAccountRequest,
            db: AsyncSession
    ) -> CandidateAccountModel:
        candidate_account = CandidateAccountModel(
            user_id=candidate.user_id
        )
        db.add(candidate_account)

        await db.commit()
        await db.refresh(candidate_account)

        return candidate_account
