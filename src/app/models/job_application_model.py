from sqlalchemy import (
    Integer,
    Text,
    DateTime,
    Boolean, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.core.database.database_helper import Base
from datetime import datetime


class JobApplicationModel(Base):
    __tablename__ = "job_applications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    cover_letter: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    rejected: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    accepted: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )
    cv_id: Mapped[int] = mapped_column(
        ForeignKey("cvs.id")
    )
    cv: Mapped["CVModel"] = relationship(
        "CVModel",
        back_populates="job_applications"
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id")
    )
    vacancy: Mapped["VacancyModel"] = relationship(
        "VacancyModel",
        back_populates="applications"
    )