from pydantic import BaseModel, Field


class CreateVacancyRequest(BaseModel):
    title: str = Field(min_length=5, max_length=50)
    description: str = Field(min_length=5, max_length=20000)
    minimal_salary: int = Field(ge=1, le=100000)
    minimal_year_exp: int = Field(ge=0, le=20)
    job_location: str = Field(min_length=1, max_length=100)


class CreateVacancyResponse(CreateVacancyRequest):
    id: int