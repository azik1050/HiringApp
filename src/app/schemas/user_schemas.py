from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    name: str = Field(min_length=5, max_length=250)


class FullUpdateUserRequest(CreateUserRequest):
    pass


class CreateUserResponse(BaseModel):
    id: int
    name: str
