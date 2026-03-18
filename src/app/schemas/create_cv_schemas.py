from pydantic import BaseModel, Field

from src.core.utils.data_generator import DataGenerator


class CreateCVRequest(BaseModel):
    title: str = Field(
        min_length=10,
        max_length=205,
        default_factory=DataGenerator.job_title
    )
    content: str = Field(
        min_length=1,
        max_length=10000,
        default_factory=DataGenerator.rand_text
    )


class CreateCVResponse(CreateCVRequest):
    id: int
