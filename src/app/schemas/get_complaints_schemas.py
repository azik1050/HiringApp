from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class Complaint(BaseModel):
    user: User
    message: str


class GetComplaintsResponse(BaseModel):
    total: int
    complaints: list[Complaint]
