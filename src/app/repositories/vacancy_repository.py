from src.app.models.vacancy_model import VacancyModel
from src.app.schemas.create_vacancy_schemas import CreateVacancyRequest
from src.core.base_classes.repository import BaseRepository


class VacancyRepository(BaseRepository):
    async def create_vacancy(
            self,
            company_id: int,
            vacancy: CreateVacancyRequest
    ) -> VacancyModel:
        new_vacancy = VacancyModel(
            company_id=company_id,
            title=vacancy.title,
            description=vacancy.description
        )

        return await self._add(new_vacancy)
