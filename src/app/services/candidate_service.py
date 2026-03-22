from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.repositories.candidate_account_repository import (
    CandidateAccountRepository
)
from src.app.repositories.cv_repository import CVRepository
from src.app.repositories.job_application_repository import JobApplicationRepository
from src.app.repositories.user_repository import UserRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
from src.app.schemas.create_cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)
from src.app.schemas.create_job_application_schemas import (
    CreateJobApplicationRequest,
    CreateJobApplicationResponse
)
from src.app.schemas.get_cvs_schemas import GetCVsResponse
from src.app.schemas.get_full_candidate_account_info_schemas import (
    GetFullCandidateAccountInfo
)
from src.app.schemas.get_all_vancancies_schemas import (
    GetAllVacanciesResponse
)
from src.app.services.mappers.candidate_service_mapper import CandidateAccountServiceMapper


class CandidateAccountService:
    def __init__(
            self,
            candidate_repo: CandidateAccountRepository,
            cv_repo: CVRepository,
            user_repo: UserRepository,
            application_repo: JobApplicationRepository,
            vacancy_repo: VacancyRepository
    ):
        self.mapper = CandidateAccountServiceMapper()
        self.candidate_repo = candidate_repo
        self.cv_repo = cv_repo
        self.user_repo = user_repo
        self.application_repo = application_repo
        self.vacancy_repo = vacancy_repo

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

        return self.mapper.created_candidate_account(candidate)

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

        return self.mapper.created_cv(created_cv)

    async def get_candidate_account_info(
            self,
            user_id: int
    ) -> GetFullCandidateAccountInfo:
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

        return self.mapper.full_candidate_info(user, candidate_account, cvs)

    async def get_cvs(
            self,
            cv_title: str,
            min_creation_date: datetime
    ) -> GetCVsResponse:
        cvs_info = await self.cv_repo.get_cvs_by_title_and_create_date(
            cv_title=cv_title,
            min_creation_date=min_creation_date
        )

        return self.mapper.all_cvs(cvs_info)

    async def create_application(
            self,
            job_application: CreateJobApplicationRequest
    ) -> CreateJobApplicationResponse:
        created_application = await self.application_repo.create_application(
            job_application=job_application
        )

        return self.mapper.created_application(created_application)

    async def get_vacancies(
            self,
            job_title: str,
            company_name: str,
            min_salary: int,
            min_years_req: int
    ) -> GetAllVacanciesResponse:
        vacancies = await self.vacancy_repo.get_vacancies(
            job_title=job_title,
            company_name=company_name,
            min_salary=min_salary,
            min_years_req=min_years_req,
        )

        return self.mapper.all_vacancies(vacancies)
