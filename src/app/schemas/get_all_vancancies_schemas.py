from pydantic import BaseModel


class Vacancy(BaseModel):
    id: int
    job_title: str
    company_name: str
    min_salary: int
    min_years_req: int
    job_location: str


class GetAllVacanciesResponse(BaseModel):
    data: list[Vacancy]
