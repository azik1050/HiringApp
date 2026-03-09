from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
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
        try:
            candidate = await CandidateAccountRepository.create_candidate_account(
                candidate=candidate_account,
                db=db
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="Account already exists")

        return CreateCandidateAccountResponse(
            id=candidate.id,
            user_id=candidate.user_id
        )

    async def create_cv(
            self,
            cv: CreateCVRequest,
            db: AsyncSession
    ) -> CreateCVResponse:
        created_cv = await CVRepository.create_cv(cv=cv, db=db)

        return CreateCVResponse(
            id=created_cv.id,
            candidate_account_id=created_cv.candidate_account_id,
            title=created_cv.title,
            content=created_cv.content
        )
