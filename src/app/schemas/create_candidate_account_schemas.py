from pydantic import BaseModel


class CreateCandidateAccountRequest(BaseModel):
    user_id: int


class CreateCandidateAccountResponse(BaseModel):
    id: int
    user_id: int
