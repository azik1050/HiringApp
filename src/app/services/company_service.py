from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from src.app.repositories.company_account_repository import CompanyAccountRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.app.schemas.create_company_account_schemas import (
    CreateCompanyAccountRequest,
    CreateCompanyAccountResponse
)
from src.app.schemas.create_vacancy_schemas import (
    CreateVacancyRequest,
    CreateVacancyResponse
)
from src.app.schemas.get_vacancy_by_id_schemas import GetVacancyByIdResponse
from src.app.services.mappers.company_service_mapper import CompanyServiceMapper


class CompanyService:
    def __init__(
            self,
            company_repo: CompanyAccountRepository,
            vacancy_repo: VacancyRepository
    ):
        self.mapper = CompanyServiceMapper()
        self.company_repo = company_repo
        self.vacancy_repo = vacancy_repo

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

    async def get_vacancy_by_id(
            self,
            vacancy_id: int
    ) -> GetVacancyByIdResponse:
        vacancy = await self.vacancy_repo.get_vacancy_by_id(
            vacancy_id=vacancy_id
        )

        if not vacancy:
            raise HTTPException(status_code=404, detail="Vacancy not found")

        return self.mapper.vacancy(vacancy)
