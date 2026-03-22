from pydantic import BaseModel, SecretStr, Field
from src.core.utils.data_generator import DataGenerator


class RegisterRequest(BaseModel):
    name: str = Field(
        min_length=5,
        max_length=30,
        default_factory=DataGenerator.name
    )
    password: str = Field(
        min_length=8,
        max_length=30,
        default_factory=DataGenerator.password
    )


class RegisterResponse(RegisterRequest):
    id: int


class LoginRequest(BaseModel):
    name: str = Field(min_length=5, max_length=30)
    password: str = Field(min_length=8, max_length=30)


class LoginResponse(BaseModel):
    access_token: str
