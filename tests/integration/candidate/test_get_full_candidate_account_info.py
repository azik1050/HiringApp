import allure
from src.app.schemas.get_full_candidate_account_info_schemas import (
    GetFullCandidateAccountInfo
)
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/info")
class TestGetFullCandidateAccountInfo(BaseAPITest):
    @allure.title("Validate candidate account info endpoint")
    async def test_get_full_candidate_account_info(self, candidate_service):
        with allure.step("Get candidate account information"):
            response = await candidate_service.get_full_candidate_account_info()
            self.assert_model(response, GetFullCandidateAccountInfo)
