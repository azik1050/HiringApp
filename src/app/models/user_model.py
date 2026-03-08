from typing import Optional
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from src.core.database.database_helper import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(30))
    candidate_account: Mapped[Optional["CandidateAccountModel"]] = relationship(
        "CandidateAccountModel",
        back_populates="user"
    )
    company_account: Mapped["CompanyAccountModel"] = relationship(
        "CompanyAccountModel",
        back_populates="owner"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
