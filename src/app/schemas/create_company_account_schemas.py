from typing import Optional
from pydantic import BaseModel, Field


class CreateCompanyAccountRequest(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    short_description: str = Field(min_length=5, max_length=250)
    long_description: Optional[str] = Field(max_length=20000)


class CreateCompanyAccountResponse(CreateCompanyAccountRequest):
    id: int

