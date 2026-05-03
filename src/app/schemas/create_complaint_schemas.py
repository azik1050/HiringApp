from pydantic import BaseModel, Field


class CreateComplaintRequest(BaseModel):
    message: str = Field(strict=False)
