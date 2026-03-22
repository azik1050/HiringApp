from authx import TokenPayload
from fastapi import APIRouter, Depends
from src.app.dependencies.services import build_candidate_service
from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
from src.app.schemas.create_cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)
from src.app.schemas.create_job_application_schemas import (
    CreateJobApplicationResponse,
    CreateJobApplicationRequest
)
from src.app.schemas.get_all_vancancies_schemas import GetAllVacanciesResponse
from src.app.schemas.get_cvs_schemas import GetCVsResponse
from src.app.schemas.get_full_candidate_account_info_schemas import (
    GetFullCandidateAccountInfo
)
from src.app.services.candidate_service import CandidateAccountService
from src.core.auth.security import security
from datetime import datetime

router = APIRouter(prefix="/candidate-account", tags=["Candidate Account Controller"])


@router.post(
    '/',
    status_code=201,
    response_model=CreateCandidateAccountResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_candidate_account(
        token: TokenPayload = Depends(security.access_token_required),
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.create_candidate_account(
        user_id=int(token.sub)
    )


@router.post(
    '/cv/',
    status_code=201,
    response_model=CreateCVResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_cv(
        cv: CreateCVRequest,
        token: TokenPayload = Depends(security.access_token_required),
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.create_cv(
        user_id=int(token.sub),
        cv=cv
    )


@router.get(
    '/info/',
    status_code=200,
    response_model=GetFullCandidateAccountInfo
)
async def get_candidate_account_info(
        token: TokenPayload = Depends(security.access_token_required),
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.get_candidate_account_info(
        user_id=int(token.sub)
    )


@router.get(
    '/cv/',
    status_code=200,
    response_model=GetCVsResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def get_all_cvs(
        cv_title: str = "",
        min_creation_date: datetime = datetime.now(),
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.get_cvs(
        cv_title=cv_title,
        min_creation_date=min_creation_date
    )


@router.post(
    '/cv/application/',
    status_code=201,
    response_model=CreateJobApplicationResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_job_application(
        job_application: CreateJobApplicationRequest,
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.create_application(
        job_application=job_application
    )


@router.get(
    '/vacancy/',
    status_code=200,
    response_model=GetAllVacanciesResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def get_all_vacancies(
        job_title: str = "",
        company_name: str = "",
        min_salary: int = 0,
        min_years_req: int = 0,
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.get_vacancies(
        job_title=job_title,
        company_name=company_name,
        min_salary=min_salary,
        min_years_req=min_years_req,
    )
