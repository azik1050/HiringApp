from typing import Optional
from pydantic import BaseModel


class ApplicationResponse(BaseModel):
    content: str


class Application(BaseModel):
    accepted: Optional[bool]
    cover_letter: str
    created_at: str
    response: Optional[ApplicationResponse]


class GetVacancyByIdResponse(BaseModel):
    id: int
    title: str
    description: str
    company_id: int
    minimal_salary: Optional[int]
    minimal_year_exp: Optional[int]
    job_location: Optional[str]
    creation_date: str
    last_update_date: str
    application: Optional[Application]
