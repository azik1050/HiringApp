import pytest
from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
import allure


@allure.parent_suite("Internal Service API")
@allure.suite("Auth Service")
@allure.sub_suite("POST /candidate-account")
@allure.title("Validate candidate account creation")
@pytest.mark.anyio
@pytest.mark.api
async def test_create_candidate_account(candidate_service):
    with allure.step("Create candidate account"):
        response = await candidate_service.create_candidate()
        assert response.status_code == 200
        CreateCandidateAccountResponse.model_validate(response.json())
