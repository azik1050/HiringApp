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
from src.app.services.candidate_service import CandidateAccountService
from src.core.auth.security import security

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


@router.get('/info/')
async def get_candidate_account_info(
        token: TokenPayload = Depends(security.access_token_required),
        candidate_service: CandidateAccountService = Depends(build_candidate_service)
):
    return await candidate_service.get_candidate_account_info(
        user_id=int(token.sub)
    )
