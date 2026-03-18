import pytest
from src.app.schemas.auth_schemas import RegisterResponse
from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
import allure
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("POST /candidate-account")
@pytest.mark.skip("Not ready")
class TestRegisterMethod(BaseAPITest):
    @allure.title("Validate candidate account creation")
    async def test_register_method(self, auth_service, candidate_service):
        with allure.step("Register new user"):
            response = await auth_service.register()
            self.assert_model(response, RegisterResponse)
        with allure.step("Login as a user"):
            pass
        with allure.step("Create candidate account"):
            response = await candidate_service.create_candidate(body=None)
            self.assert_model(response, CreateCandidateAccountResponse)
