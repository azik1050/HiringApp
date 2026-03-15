from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
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


class CompanyService:
    def __init__(
            self,
            company_repo: CompanyAccountRepository,
            vacancy_repo: VacancyRepository
    ):
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

        return CreateCompanyAccountResponse(
            id=company_account.id,
            name=company_account.name,
            short_description=company_account.short_description,
            long_description=company_account.long_description
        )

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

        return CreateVacancyResponse(
            id=new_vacancy.id,
            title=new_vacancy.title,
            description=new_vacancy.description
        )
