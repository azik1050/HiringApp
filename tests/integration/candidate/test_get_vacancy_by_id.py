import allure
from src.app.schemas.get_vacancy_by_id_schemas import GetVacancyByIdResponse
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/vacancy/{vacancy_id}")
class TestGetCandidateInfo(BaseAPITest):
    @allure.title("Validate vacancy")
    async def test_get_cvs_method(self, auth_service, candidate_service):
        with allure.step("Get vacancy by id"):
            response = await candidate_service.get_vacancy_by_id(
                vacancy_id=1
            )
            self.assert_model(response, GetVacancyByIdResponse)
