from src.core.database.database_helper import Base
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CandidateAccountModel(Base):
    __tablename__ = "candidate_accounts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True
    )
    user: Mapped["UserModel"] = relationship(
        "UserModel",
        back_populates="candidate_account"
    )
    cvs: Mapped[list["CVModel"]] = relationship(
        back_populates="candidate"
    )