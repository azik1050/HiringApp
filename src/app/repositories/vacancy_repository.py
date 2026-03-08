from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.vacancy_model import VacancyModel
from src.app.schemas.vacancy_schemas import CreateVacancyRequest


class VacancyRepository:
    @staticmethod
    async def create_vacancy(
            vacancy: CreateVacancyRequest,
            db: AsyncSession
    ) -> VacancyModel:
        new_vacancy = VacancyModel(
            company_id=vacancy.company_id,
            title=vacancy.title,
            description=vacancy.description
        )

        db.add(new_vacancy)
        await db.commit()
        await db.refresh(new_vacancy)

        return new_vacancy
