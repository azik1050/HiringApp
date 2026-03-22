import allure
from src.app.schemas.get_cvs_schemas import GetCVsResponse
from tests.integration.base_api_test import BaseAPITest
from datetime import datetime


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/cv/all")
class TestGetFullCandidateAccountInfo(BaseAPITest):
    @allure.title("Validate candidate account cvs endpoint")
    async def test_get_candidate_cvs(self, candidate_service):
        with allure.step("Get candidate account CVs"):
            response = await candidate_service.get_candidate_account_cvs(
                params={
                    'cv_title': "Mobility",
                    'min_creation_date': datetime.fromisocalendar(
                        year=2026,
                        week=3,
                        day=5
                    )
                }
            )
            self.assert_model(response, GetCVsResponse)
