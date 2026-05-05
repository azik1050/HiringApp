from pydantic import BaseModel, Field


class CreateComplaintRequest(BaseModel):
    message: str = Field(strict=False)


class CreateComplaintResponse(BaseModel):
    id: int
    message: str
    user_id: int

