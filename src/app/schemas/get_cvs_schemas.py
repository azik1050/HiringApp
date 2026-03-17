from pydantic import BaseModel


class CVdata(BaseModel):
    owner_name: str
    title: str


class GetCVsResponse(BaseModel):
    data: list[CVdata]
