from authx import TokenPayload
from fastapi import APIRouter
from fastapi.params import Depends
from src.app.dependencies.services import build_company_service
from src.app.schemas.create_company_account_schemas import (
    CreateCompanyAccountResponse,
    CreateCompanyAccountRequest
)
from src.app.schemas.create_vacancy_schemas import (
    CreateVacancyResponse,
    CreateVacancyRequest
)
from src.app.services.company_service import CompanyService
from src.core.auth.security import security

router = APIRouter(prefix="/company", tags=["Company Account Controller"])


@router.post(
    '/',
    status_code=201,
    response_model=CreateCompanyAccountResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_company_account(
        company: CreateCompanyAccountRequest,
        token: TokenPayload = Depends(security.access_token_required),
        company_service: CompanyService = Depends(build_company_service)
):
    return await company_service.create_company(
        user_id=int(token.sub),
        company=company
    )


@router.post(
    '/vacancy/',
    status_code=201,
    response_model=CreateVacancyResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_vacancy(
        vacancy: CreateVacancyRequest,
        token: TokenPayload = Depends(security.access_token_required),
        company_service: CompanyService = Depends(build_company_service)
):
    return await company_service.create_vacancy(
        user_id=int(token.sub),
        vacancy=vacancy
    )
