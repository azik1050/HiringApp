from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.company_account_repository import CompanyAccountRepository
from src.app.repositories.cv_repository import CVRepository
from src.app.repositories.user_repository import UserRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.core.database.database_helper import DataBase


def build_user_repo(
        session: AsyncSession = Depends(DataBase.get_db)
):
    """Returns created UserRepository object"""
    return UserRepository(session=session)


def build_candidate_account_repo(
        session: AsyncSession = Depends(DataBase.get_db)
):
    """Returns created CandidateAccountRepository object"""
    return CandidateAccountRepository(session=session)


def build_company_repo(
        session: AsyncSession = Depends(DataBase.get_db)
):
    """Returns created CompanyAccountRepository object"""
    return CompanyAccountRepository(session=session)


def build_vacancy_repo(
        session: AsyncSession = Depends(DataBase.get_db)
):
    """Returns created VacancyRepository object"""
    return VacancyRepository(session=session)


def build_cv_repo(
        session: AsyncSession = Depends(DataBase.get_db)
):
    """Returns created CVRepository object"""
    return CVRepository(session=session)
