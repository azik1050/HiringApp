import allure
from src.app.schemas.get_all_vancancies_schemas import (
    GetAllVacanciesResponse
)
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("GET /candidate-account/vacancy")
class TestGetCandidateInfo(BaseAPITest):
    @allure.title("Validate vacancies")
    async def test_get_cvs_method(self, auth_service, candidate_service):
        with allure.step("Get all vacancies"):
            response = await candidate_service.get_vacancies()
            self.assert_model(response, GetAllVacanciesResponse)
