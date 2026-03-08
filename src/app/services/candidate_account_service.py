from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.cv_repository import CVRepository
from src.app.schemas.candidate_account_schemas import (
    CreateCandidateAccountRequest,
    CreateCandidateAccountResponse
)
from src.app.schemas.cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)


class CandidateAccountService:
    async def create_candidate_account(
            self,
            candidate_account: CreateCandidateAccountRequest,
            db: AsyncSession
    ) -> CreateCandidateAccountResponse:
        candidate = await CandidateAccountRepository.create_candidate_account(
            candidate=candidate_account,
            db=db
        )
        return CreateCandidateAccountResponse(
            id=candidate.id,
            user_id=candidate.user_id
        )

    async def create_cv(
            self,
            cv: CreateCVRequest,
            db: AsyncSession
    ) -> CreateCVResponse:
        created_cv = await CVRepository.create_cv(cv, db)
        return CreateCVResponse(
            id=created_cv.id,
            candidate_account_id=created_cv.candidate_account_id,
            title=created_cv.title,
            content=created_cv.content
        )


