import allure
from src.app.schemas.create_cv_schemas import CreateCVResponse, CreateCVRequest
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Candidate Account Service")
@allure.sub_suite("POST /candidate-account/cv")
class TestCreateCV(BaseAPITest):
    @allure.title("Create valid CV")
    async def test_register_method(self, candidate_service):
        with allure.step("Create CV"):
            response = await candidate_service.create_cv(
                body=CreateCVRequest().model_dump()
            )
            self.assert_model(response, CreateCVResponse)
