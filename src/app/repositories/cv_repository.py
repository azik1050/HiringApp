from sqlalchemy import select
from src.app.models import CVModel, UserModel, CandidateAccountModel
from src.app.schemas.create_cv_schemas import CreateCVRequest
from src.app.schemas.get_cvs_schemas import CVdata
from src.core.entities.repository import BaseRepository
from datetime import datetime


class CVRepository(BaseRepository):
    async def create_cv(
            self,
            candidate_account_id: int,
            cv: CreateCVRequest
    ) -> CVModel:
        new_cv = CVModel(
            candidate_account_id=candidate_account_id,
            title=cv.title,
            content=cv.content
        )

        return await self._add(new_cv)

    async def get_cvs(
            self,
            candidate_account_id: int,
    ) -> list[CVModel]:
        query = (
            select(CVModel)
            .where(CVModel.candidate_account_id == candidate_account_id)
            .order_by(CVModel.updated_at.desc())
        )

        return await self._find_all(query)

    async def get_cvs_by_title_and_create_date(
            self,
            cv_title: str,
            min_creation_date: datetime
    ) -> list[CVdata]:
        query = (
            select(
                UserModel.name.label("owner_name"),
                CVModel.title.label("title"),
            )
            .join(
                CandidateAccountModel,
                CVModel.candidate_account_id == CandidateAccountModel.id
            )
            .join(
                UserModel,
                CandidateAccountModel.user_id == CandidateAccountModel.id
            )
            .where(
                CVModel.created_at >= min_creation_date,
                CVModel.title.contains(cv_title)
            )
            .order_by(CVModel.created_at.desc())
        )

        result = await self._session.execute(query)

        return [
            CVdata(
                owner_name=cv["owner_name"],
                title=cv["title"],
            )
            for cv in result.mappings().all()
        ]

