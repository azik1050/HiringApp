from typing import Optional

from pydantic import BaseModel


class VacancyApplication(BaseModel):
    id: int
    candidate_name: str
    accepted: Optional[bool]
    cover_letter: str
    created_at: str


class GetCompanyVacancyByIdResponse(BaseModel):
    id: int
    title: str
    description: str
    minimal_salary: int
    minimal_year_exp: int
    job_location: str
    creation_date: str
    last_update_date: str
    applications: list[VacancyApplication]
