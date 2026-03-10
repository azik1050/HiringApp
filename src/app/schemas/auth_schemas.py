from pydantic import BaseModel, SecretStr
from pydantic.v1 import Field


class RegisterRequest(BaseModel):
    name: str = Field(min_length=5, max_length=30)
    password: str = Field(min_length=8, max_length=30)


class ResponseResponse(BaseModel):
    id: int


class LoginRequest(BaseModel):
    name: str = Field(min_length=5, max_length=30)
    password: str = Field(min_length=8, max_length=30)


class LoginResponse(BaseModel):
    access_token: str
