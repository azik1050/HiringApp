import allure
from src.app.schemas.get_cvs_schemas import GetCVsResponse
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/cv")
class TestGetCandidateInfo(BaseAPITest):
    @allure.title("Validate cvs")
    async def test_get_cvs_method(self, auth_service, candidate_service):
        with allure.step("Get cvs information"):
            response = await candidate_service.get_all_cvs()
            self.assert_model(response, GetCVsResponse)
