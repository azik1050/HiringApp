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
from src.app.schemas.get_all_vancancies_schemas import (
    GetAllVacanciesResponse,
    Vacancy
)
from src.app.schemas.get_vacancy_by_id_schemas import GetVacancyByIdResponse


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
            description=new_vacancy.description,
            minimal_salary=new_vacancy.minimal_salary,
            minimal_year_exp=new_vacancy.minimal_year_exp,
            job_location=new_vacancy.job_location
        )

    async def get_vacancies(
            self,
            job_title: str ,
            company_name: str ,
            min_salary: int,
            min_years_req: int
    ):
        vacancies_info = await self.vacancy_repo.get_vacancies(
            job_title=job_title,
            company_name=company_name,
            min_salary=min_salary,
            min_years_req=min_years_req,
        )

        return GetAllVacanciesResponse(
            data=[
                Vacancy(
                    id=vacancy['id'],
                    job_title=vacancy['job_title'],
                    company_name=vacancy['company_name'],
                    min_salary=vacancy['min_salary'],
                    min_years_req=vacancy['min_years_req'],
                    job_location=vacancy['job_location']
                    )
                for vacancy in vacancies_info
            ]
        )

    async def get_vacancy_by_id(self, vacancy_id: int):
        vacancy = await self.vacancy_repo.get_vacancy_by_id(
            vacancy_id=vacancy_id
        )

        if not vacancy:
            raise HTTPException(
                status_code=404,
                detail="Vacancy not found"
            )

        return GetVacancyByIdResponse(
            title=vacancy.title,
            description=vacancy.description,
            company_id=vacancy.company_id,
            minimal_salary=vacancy.minimal_salary,
            minimal_year_exp=vacancy.minimal_year_exp,
            job_location=vacancy.job_location,
            creation_date=str(vacancy.creation_date),
            last_update_date=str(vacancy.last_update_date)
        )


