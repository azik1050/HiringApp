from typing import Optional
from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    name: str = Field(min_length=5, max_length=250)
    password: str =Field(min_length=8, max_length=30)


class FullUpdateUserRequest(CreateUserRequest):
    pass


class CreateUserResponse(BaseModel):
    id: int
    name: str


class User(BaseModel):
    id: int
    name: str


class GetUsersResponse(BaseModel):
    data: list[User]


class GetUserResponse(BaseModel):
    id: int
    name: str
    candidate_account_id: Optional[int]
