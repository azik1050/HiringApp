from pydantic import BaseModel, Field


class CreateInvitationRequest(BaseModel):
    message: str = Field(min_length=0, max_length=255)
    job_application_id: int


class CreateInvitationResponse(CreateInvitationRequest):
    id: int
