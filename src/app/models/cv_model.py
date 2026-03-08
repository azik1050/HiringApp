from sqlalchemy import (
    Integer,
    ForeignKey,
    Text,
    String,
    DateTime
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.database.database_helper import Base
from datetime import datetime
from sqlalchemy.sql import func


class CVModel(Base):
    __tablename__ = "cvs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    candidate: Mapped["CandidateAccountModel"] = relationship(
        back_populates="cvs"
    )
    candidate_account_id: Mapped[int] = mapped_column(
        ForeignKey("candidate_accounts.id")
    )
    job_applications: Mapped[list["JobApplicationModel"]] = relationship(
        back_populates="cv"
    )
    title: Mapped[str] = mapped_column(
        String(250)
    )
    content: Mapped[str] = mapped_column(
        Text
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )


