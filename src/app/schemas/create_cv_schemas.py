from pydantic import BaseModel, Field


class CreateCVRequest(BaseModel):
    title: str = Field(min_length=10, max_length=205)
    content: str = Field(min_length=1, max_length=10000)


class CreateCVResponse(CreateCVRequest):
    id: int


