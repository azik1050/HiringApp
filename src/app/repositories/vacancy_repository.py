from typing import Optional
from sqlalchemy import select
from src.app.models import CompanyAccountModel
from src.app.models.vacancy_model import VacancyModel
from src.app.schemas.create_vacancy_schemas import CreateVacancyRequest
from src.app.repositories._base_repository import BaseRepository


class VacancyRepository(BaseRepository):
    async def create_vacancy(
            self,
            company_id: int,
            vacancy: CreateVacancyRequest
    ) -> VacancyModel:
        new_vacancy = VacancyModel(
            company_id=company_id,
            title=vacancy.title,
            description=vacancy.description,
            minimal_salary=vacancy.minimal_salary,
            minimal_year_exp=vacancy.minimal_year_exp,
            job_location=vacancy.job_location
        )

        return await self._add(new_vacancy)

    async def get_vacancies(
            self,
            job_title: str ,
            company_name: str ,
            min_salary: int,
            min_years_req: int
    ):
        query = (
            select(
                VacancyModel.id,
                VacancyModel.title.label("job_title"),
                VacancyModel.minimal_salary.label("min_salary"),
                VacancyModel.minimal_year_exp.label("min_years_req"),
                VacancyModel.job_location.label("job_location"),
                CompanyAccountModel.name.label("company_name")
            )
            .join(CompanyAccountModel, CompanyAccountModel.id == VacancyModel.company_id)
            .where(VacancyModel.title.ilike(f"%{job_title}%"))
            .where(CompanyAccountModel.name.ilike(f"%{company_name}%"))
            .where(VacancyModel.minimal_salary >= min_salary)
            .where(VacancyModel.minimal_year_exp >= min_years_req)
            .order_by(VacancyModel.last_update_date.desc())
        )

        result = await self._session.execute(query)

        return result.mappings().all()

    async def get_vacancy_by_id(
            self,
            vacancy_id: int
    ) -> Optional[VacancyModel]:
        query = (
            select(
                VacancyModel
            )
            .where(VacancyModel.id == vacancy_id)
        )

        return await self._find_one(query)