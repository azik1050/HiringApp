from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.company_account_repository import CompanyAccountRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.app.schemas.company_account_schemas import (
    CreateCompanyAccountRequest,
    CreateCompanyAccountResponse
)
from src.app.schemas.vacancy_schemas import (
    CreateVacancyRequest,
    CreateVacancyResponse
)


class CompanyService:
    async def create_company(
            self,
            company: CreateCompanyAccountRequest,
            db: AsyncSession
    ) -> CreateCompanyAccountResponse:
        company_account = await CompanyAccountRepository.create_company_account(
            company=company,
            db=db
        )

        return CreateCompanyAccountResponse(
            id=company_account.id,
            name=company_account.name,
            short_description=company_account.short_description,
            long_description=company_account.long_description,
            owner_id=company_account.owner_id,
        )

    async def create_vacancy(
            self,
            vacancy: CreateVacancyRequest,
            db: AsyncSession
    ) -> CreateVacancyResponse:
        new_vacancy = await VacancyRepository.create_vacancy(
            vacancy=vacancy,
            db=db
        )

        return CreateVacancyResponse(
            id=new_vacancy.id,
            title=new_vacancy.title,
            description=new_vacancy.description,
            company_id=new_vacancy.company_id,
        )