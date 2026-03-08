from src.core.database.database_helper import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import (
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)
from datetime import datetime
from sqlalchemy.sql import func


class VacancyModel(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    applications: Mapped[list["JobApplicationModel"]] = relationship(
        "JobApplicationModel",
        back_populates="vacancy"
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("company_accounts.id")
    )
    company: Mapped["CompanyAccountModel"] = relationship(
        "CompanyAccountModel",
        back_populates="vacancies"
    )
    creation_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    last_update_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

