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
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/company", tags=["Company Account Controller"])
service = CompanyService()


@router.post('/', status_code=201, response_model=CreateCompanyAccountResponse)
async def create_company_account(
        company: CreateCompanyAccountRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_company(
        company=company,
        db=db
    )


@router.post('/vacancy/', status_code=201, response_model=CreateVacancyResponse)
async def create_vacancy(
        vacancy: CreateVacancyRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_vacancy(
        vacancy=vacancy,
        db=db
    )
