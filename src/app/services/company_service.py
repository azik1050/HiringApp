from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
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
            user_id: int,
            company: CreateCompanyAccountRequest,
            db: AsyncSession
    ) -> CreateCompanyAccountResponse:
        try:
            company_account = await CompanyAccountRepository.create_company_account(
                user_id=user_id,
                company=company,
                db=db
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
            vacancy: CreateVacancyRequest,
            db: AsyncSession
    ) -> CreateVacancyResponse:
        company = await CompanyAccountRepository.get_company_id_by_user_id(
            user_id=user_id,
            db=db
        )

        new_vacancy = await VacancyRepository.create_vacancy(
            company_id=company['company_id'],
            vacancy=vacancy,
            db=db
        )

        return CreateVacancyResponse(
            id=new_vacancy.id,
            title=new_vacancy.title,
            description=new_vacancy.description,
            company_id=new_vacancy.company_id,
        )
