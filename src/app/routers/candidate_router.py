from authx import TokenPayload
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.schemas.candidate_account_schemas import (
    CreateCandidateAccountResponse
)
from src.app.schemas.cv_schemas import (
    CreateCVRequest,
    CreateCVResponse
)
from src.app.services.candidate_service import CandidateAccountService
from src.core.auth.security import security
from src.core.database.database_helper import DataBase

router = APIRouter(prefix="/candidate-account", tags=["Candidate Account Controller"])
service = CandidateAccountService()


@router.post(
    '/',
    status_code=201,
    response_model=CreateCandidateAccountResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_candidate_account(
        token: TokenPayload = Depends(security.access_token_required),
        db: AsyncSession = Depends(DataBase.get_db)
):
    return await service.create_candidate_account(
        user_id=int(token.sub),
        db=db
    )


@router.post(
    '/cv/',
    status_code=201,
    response_model=CreateCVResponse,
    dependencies=[Depends(security.access_token_required)]
)
async def create_cv(
        cv: CreateCVRequest,
        db: AsyncSession = Depends(DataBase.get_db),
        token: TokenPayload = Depends(security.access_token_required)
):
    return await service.create_cv(
        user_id=int(token.sub),
        cv=cv,
        db=db
    )
