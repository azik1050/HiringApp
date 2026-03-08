from sqlalchemy import (
    Integer,
    String,
    Boolean,
    ForeignKey,
    Text
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from src.app.models.vacancy_model import VacancyModel
from src.core.database.database_helper import Base


class CompanyAccountModel(Base):
    __tablename__ = "company_accounts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100))
    short_description: Mapped[str] = mapped_column(String(250))
    long_description: Mapped[str] = mapped_column(Text, nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    owner: Mapped["UserModel"] = relationship(
        "UserModel",
        back_populates="company_account"
    )
    vacancies: Mapped["VacancyModel"] = relationship(
        "VacancyModel",
        back_populates="company"
    )
