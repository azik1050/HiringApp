from datetime import datetime
from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    DateTime,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database.database_helper import Base


class InvitationModel(Base):
    __tablename__ = "invitations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    message: Mapped[str] = mapped_column(
        String(255)
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id")
    )
    vacancy: Mapped["VacancyModel"] = relationship(
        "VacancyModel",
        back_populates="invitations"
    )
    job_application_id: Mapped[int] = mapped_column(
        ForeignKey("job_applications.id"),
        unique=True
    )
    job_application: Mapped["JobApplicationModel"] = relationship(
        "JobApplicationModel",
        back_populates="invitation"
    )
    creation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
