from sqlalchemy import select
from src.app.models import CVModel
from src.app.schemas.create_cv_schemas import CreateCVRequest
from src.core.base_classes.repository import BaseRepository


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