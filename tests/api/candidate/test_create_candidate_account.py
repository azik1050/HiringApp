from src.app.schemas.create_candidate_account_schemas import (
    CreateCandidateAccountResponse
)
import allure
from tests.api.base_api_test import BaseAPITest


class TestRegisterMethod(BaseAPITest):
    @allure.suite("Candidate Account Service")
    @allure.sub_suite("POST /candidate-account")
    @allure.title("Validate candidate account creation")
    async def test_register_method(self, candidate_service):
        with allure.step("Create candidate account"):
            response = await candidate_service.create_candidate()
            self.assert_model(response, CreateCandidateAccountResponse)
