from authx import TokenPayload
from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.company_account_schemas import (
    CreateCompanyAccountResponse,
    CreateCompanyAccountRequest
)
from src.app.schemas.vacancy_schemas import (
    CreateVacancyResponse,
    CreateVacancyRequest
)
from src.app.services.company_service import CompanyService
from src.core.auth.security import security
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/company", tags=["Company Account Controller"])
service = CompanyService()


@router.post(
    '/',
    status_code=201,
    response_model=CreateCompanyAccountResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_company_account(
        company: CreateCompanyAccountRequest,
        db: AsyncSession = Depends(DataBase.get_db),
        token: TokenPayload = Depends(security.access_token_required)
):
    return await service.create_company(
        user_id=int(token.sub),
        company=company,
        db=db
    )


@router.post(
    '/vacancy/',
    status_code=201,
    response_model=CreateVacancyResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_vacancy(
        vacancy: CreateVacancyRequest,
        db: AsyncSession = Depends(DataBase.get_db),
        token: TokenPayload = Depends(security.access_token_required)
):
    return await service.create_vacancy(
        user_id=int(token.sub),
        vacancy=vacancy,
        db=db
    )
