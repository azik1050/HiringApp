from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.cv_repository import CVRepository
from src.app.repositories.user_repository import UserRepository
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
            user_id: int,
            db: AsyncSession
    ) -> CreateCandidateAccountResponse:
        try:
            candidate = await CandidateAccountRepository.create_candidate_account(
                user_id=user_id,
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
            user_id: int,
            cv: CreateCVRequest,
            db: AsyncSession
    ) -> CreateCVResponse:
        candidate_account = await CandidateAccountRepository.get_candidate_account_id(
            user_id=user_id,
            db=db
        )

        created_cv = await CVRepository.create_cv(
            candidate_account_id=candidate_account['id'],
            cv=cv,
            db=db
        )

        return CreateCVResponse(
            id=created_cv.id,
            title=created_cv.title,
            content=created_cv.content
        )
