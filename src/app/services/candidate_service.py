from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.cv_repository import CVRepository
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
from src.app.schemas.create_cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)
from src.app.schemas.get_full_candidate_account_info import (
    GetFullCandidateAccountInfo,
    CV
)


class CandidateAccountService:
    def __init__(
            self,
            candidate_repo: CandidateAccountRepository,
            cv_repo: CVRepository,
            user_repo: UserRepository
    ):
        self.candidate_repo = candidate_repo
        self.cv_repo = cv_repo
        self.user_repo = user_repo

    async def create_candidate_account(
            self,
            user_id: int
    ) -> CreateCandidateAccountResponse:
        try:
            candidate = await self.candidate_repo.create_candidate_account(
                user_id=user_id
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
    ) -> CreateCVResponse:
        candidate_account = await self.candidate_repo.get_candidate_account_id(
            user_id=user_id
        )

        created_cv = await self.cv_repo.create_cv(
            candidate_account_id=candidate_account['id'],
            cv=cv
        )

        return CreateCVResponse(
            id=created_cv.id,
            title=created_cv.title,
            content=created_cv.content
        )

    async def get_candidate_account_info(
            self,
            user_id: int
    ):
        user = await self.user_repo.get_user(user_id=user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        candidate_account = await self.candidate_repo.get_candidate_account(
            user_id=user_id
        )

        if not candidate_account:
            raise HTTPException(status_code=404, detail="Candidate account not found")

        cvs = await self.cv_repo.get_cvs(
            candidate_account_id=candidate_account.id
        )

        return GetFullCandidateAccountInfo(
            user_id=user.id,
            name=user.name,
            candidate_account_id=candidate_account.id,
            registration_date=str(user.created_at),
            cvs=[
                CV(
                    id=cv.id,
                    title=cv.title,
                    last_update=str(cv.updated_at)
                )
                for cv in cvs
            ]
        )

