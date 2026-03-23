from pydantic import BaseModel


class Vacancy(BaseModel):
    id: int
    title: str
    description: str
    last_update_date: str


class GetCompanyInfoResponse(BaseModel):
    id: int
    name: str
    short_description: str
    full_description: str
    vacancies: list[Vacancy]
