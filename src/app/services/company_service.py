from typing import Optional
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.models import VacancyModel
from src.app.repositories.company_account_repository import CompanyAccountRepository
from src.app.repositories.job_application_repository import JobApplicationRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.app.schemas.create_company_account_schemas import (
    CreateCompanyAccountRequest,
    CreateCompanyAccountResponse
)
from src.app.schemas.create_vacancy_schemas import (
    CreateVacancyRequest,
    CreateVacancyResponse
)
from src.app.schemas.get_company_vacancy_by_id import GetCompanyVacancyByIdResponse
from src.app.services.mappers.company_service_mapper import CompanyServiceMapper


class CompanyService:
    def __init__(
            self,
            company_repo: CompanyAccountRepository,
            vacancy_repo: VacancyRepository,
            application_repo: JobApplicationRepository,
    ):
        self.mapper = CompanyServiceMapper()
        self.company_repo = company_repo
        self.vacancy_repo = vacancy_repo
        self.application_repo = application_repo

    async def create_company(
            self,
            user_id: int,
            company: CreateCompanyAccountRequest
    ) -> CreateCompanyAccountResponse:
        try:
            company_account = await self.company_repo.create_company_account(
                user_id=user_id,
                company=company
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="User already has a company")

        return self.mapper.created_company(company_account)

    async def create_vacancy(
            self,
            user_id: int,
            vacancy: CreateVacancyRequest
    ) -> CreateVacancyResponse:
        company = await self.company_repo.get_company_id_by_user_id(
            user_id=user_id
        )

        new_vacancy = await self.vacancy_repo.create_vacancy(
            company_id=company['company_id'],
            vacancy=vacancy
        )

        return self.mapper.created_vacancy(new_vacancy)

    async def get_company_info(
            self,
            owner_id
    ):
        company_info = await self.company_repo.get_company_by_owner_id(owner_id)
        if not company_info:
            raise HTTPException(status_code=404, detail="Company does not exist")

        vacancies = await self.vacancy_repo.get_vacancies_by_owner_id(owner_id)

        return self.mapper.company_info(company_info, vacancies)

    async def get_company_vacancy_by_id(
            self,
            user_id: int,
            vacancy_id: int
    ) -> GetCompanyVacancyByIdResponse:
        vacancies = await self.vacancy_repo.get_vacancies_by_owner_id(owner_id=user_id) # get all owners vacancies

        vacancy: Optional[VacancyModel] = None
        for company_vac in vacancies:
            if company_vac.id == vacancy_id:
                vacancy = company_vac
                break

        if not vacancy: # Check that company is vacancy owner
            raise HTTPException(status_code=403, detail="Only owner can view vacancy")

        applications_info = await self.application_repo.get_applications_info_by_vacancy_id(
            vacancy_id=vacancy_id
        )

        return self.mapper.company_vacancy(vacancy, applications_info)