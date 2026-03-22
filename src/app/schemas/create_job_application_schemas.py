from pydantic import BaseModel


class CreateJobApplicationRequest(BaseModel):
    cover_letter: str
    cv_id: int
    vacancy_id: int


class CreateJobApplicationResponse(CreateJobApplicationRequest):
    id: int
