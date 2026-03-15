from pydantic import BaseModel, Field


class CreateVacancyRequest(BaseModel):
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=5, max_length=20000)


class CreateVacancyResponse(CreateVacancyRequest):
    id: int