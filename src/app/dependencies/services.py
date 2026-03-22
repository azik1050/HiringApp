from fastapi import Depends
from src.app.dependencies.repositories import (
    build_user_repo,
    build_candidate_account_repo,
    build_vacancy_repo,
    build_company_repo,
    build_cv_repo,
    build_job_application_repo
)
from src.app.repositories.candidate_account_repository import CandidateAccountRepository
from src.app.repositories.company_account_repository import CompanyAccountRepository
from src.app.repositories.cv_repository import CVRepository
from src.app.repositories.job_application_repository import JobApplicationRepository
from src.app.repositories.user_repository import UserRepository
from src.app.repositories.vacancy_repository import VacancyRepository
from src.app.services.auth_service import AuthService
from src.app.services.candidate_service import CandidateAccountService
from src.app.services.company_service import CompanyService
from src.app.services.user_service import UserService


def build_auth_service(
        user_repo: UserRepository = Depends(build_user_repo)
):
    """Returns created AuthService"""
    return AuthService(
        user_repo=user_repo
    )


def build_candidate_service(
        candidate_repo: CandidateAccountRepository = Depends(build_candidate_account_repo),
        cv_repo: CVRepository = Depends(build_cv_repo),
        user_repo: UserRepository = Depends(build_user_repo),
        application_repo: JobApplicationRepository = Depends(build_job_application_repo),
        vacancy_repo: VacancyRepository = Depends(build_vacancy_repo)
):
    """Returns created CandidateService"""
    return CandidateAccountService(
        candidate_repo=candidate_repo,
        cv_repo=cv_repo,
        user_repo=user_repo,
        application_repo=application_repo,
        vacancy_repo=vacancy_repo
    )


def build_user_service(
        user_repo: UserRepository = Depends(build_user_repo)
):
    """Returns created UserService"""
    return UserService(
        user_repo=user_repo
    )


def build_company_service(
        company_repo: CompanyAccountRepository = Depends(build_company_repo),
        vacancy_repo: VacancyRepository = Depends(build_vacancy_repo)
):
    """Returns created CompanyService"""
    return CompanyService(
        company_repo=company_repo,
        vacancy_repo=vacancy_repo
    )
