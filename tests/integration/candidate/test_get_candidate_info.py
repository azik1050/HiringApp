import allure
from src.app.schemas.get_full_candidate_account_info_schemas import (
    GetFullCandidateAccountInfo
)
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/info")
class TestGetCandidateInfo(BaseAPITest):
    @allure.title("Validate candidate info")
    async def test_get_candidate_info_method(self, auth_service, candidate_service):
        with allure.step("Get candidate information"):
            response = await candidate_service.get_candidate_info()
            self.assert_model(response, GetFullCandidateAccountInfo)
