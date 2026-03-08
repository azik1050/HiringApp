from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.candidate_account_schemas import (
    CreateCandidateAccountResponse,
    CreateCandidateAccountRequest
)
from src.app.schemas.cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)
from src.app.services.candidate_service import CandidateAccountService
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/candidate_account", tags=["Candidate Account Controller"])
service = CandidateAccountService()


@router.post('/', status_code=201, response_model=CreateCandidateAccountResponse)
async def create_candidate_account(
        candidate_account: CreateCandidateAccountRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_candidate_account(
        candidate_account=candidate_account,
        db=db
    )


@router.post('/cv/', status_code=201, response_model=CreateCVResponse)
async def create_cv(
        cv: CreateCVRequest,
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_cv(cv=cv, db=db)
