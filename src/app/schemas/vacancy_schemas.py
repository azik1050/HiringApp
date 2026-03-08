from pydantic import BaseModel, Field


class CreateVacancyRequest(BaseModel):
    company_id: int = Field(ge=1)
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=5, max_length=20000)


class CreateVacancyResponse(CreateVacancyRequest):
    id: int