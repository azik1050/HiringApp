from pydantic import BaseModel


class CV(BaseModel):
    id: int
    title: str
    last_update: str


class GetFullCandidateAccountInfo(BaseModel):
    user_id: int
    name: str
    candidate_account_id: int
    registration_date: str
    cvs: list[CV]
