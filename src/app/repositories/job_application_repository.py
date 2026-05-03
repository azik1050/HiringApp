from typing import Optional

from sqlalchemy import select, update
from src.app.models import (
    JobApplicationModel,
    UserModel,
    VacancyModel,
    CompanyAccountModel, CVModel, CandidateAccountModel
)
from src.app.schemas.create_job_application_schemas import CreateJobApplicationRequest
from src.app.repositories._base_repository import BaseRepository


class JobApplicationRepository(BaseRepository):
    async def create_application(
            self,
            job_application: CreateJobApplicationRequest
    ) -> JobApplicationModel:
        instance = JobApplicationModel(
            cover_letter=job_application.cover_letter,
            vacancy_id=job_application.vacancy_id,
            cv_id=job_application.cv_id
        )

        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)

        return instance

    async def get_applications_by_vacancy_id(
            self,
            vacancy_id: int
    ) -> list[JobApplicationModel]:
        query = (
            select(
                JobApplicationModel
            )
            .where(JobApplicationModel.vacancy_id == vacancy_id)
            .order_by(JobApplicationModel.created_at.asc())
        )

        result = await self._session.execute(query)

        return self._find_all(query)

    async def get_applications_info_by_vacancy_id(
            self,
            vacancy_id: int
    ) -> dict:
        query = (
            select(
                JobApplicationModel.id,
                UserModel.name.label("candidate_name"),
                JobApplicationModel.accepted,
                JobApplicationModel.cover_letter,
                JobApplicationModel.created_at,
            )
            .join(
                VacancyModel, JobApplicationModel.vacancy_id == VacancyModel.id
            )
            .join(
                CompanyAccountModel, VacancyModel.company_id == CompanyAccountModel.id
            )
            .join(
                UserModel, CompanyAccountModel.owner_id == UserModel.id
            )
            .where(JobApplicationModel.vacancy_id == vacancy_id)
        )

        result = await self._session.execute(query)

        return result.mappings().all()

    async def get_application_by_id(
            self,
            application_id: int
    ) -> Optional[JobApplicationModel]:
        query = (
            select(JobApplicationModel)
            .where(JobApplicationModel.id == application_id)
        )
        result = await self._session.execute(query)

        return result.scalars().one_or_none()

    async def set_application_accepted(
            self,
            application_id: int
    ) -> None:
        query = (
            update(JobApplicationModel)
            .where(JobApplicationModel.id == application_id)
            .values(accepted=True)
        )
        await self._session.execute(query)
        await self._session.commit()

    async def get_candidate_vacancy_application(
            self,
            user_id: int,
            vacancy_id: int
    ) -> Optional[JobApplicationModel]:
        query = (
            select(JobApplicationModel)
            .join(CVModel, CVModel.id == JobApplicationModel.cv_id)
            .join(CandidateAccountModel, CandidateAccountModel.id == CVModel.candidate_account_id)
            .join(UserModel, UserModel.id == user_id)
            .where(JobApplicationModel.vacancy_id == vacancy_id)
            .where(CVModel.candidate_account_id == CandidateAccountModel.id)
            .where(UserModel.id == CandidateAccountModel.user_id)
        )
        return await self._find_one(query)
