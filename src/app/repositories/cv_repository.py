from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models import CVModel
from src.app.schemas.cv_schemas import CreateCVRequest


class CVRepository:
    @staticmethod
    async def create_cv(
            cv: CreateCVRequest,
            db: AsyncSession
    ) -> CVModel:
        new_cv = CVModel(
            candidate_account_id=cv.candidate_account_id,
            title=cv.title,
            content=cv.content
        )

        db.add(new_cv)
        await db.commit()
        await db.refresh(new_cv)

        return new_cv