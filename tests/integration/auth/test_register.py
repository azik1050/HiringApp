import allure
from src.app.schemas.auth_schemas import (
    RegisterRequest,
    RegisterResponse
)

from tests.integration.base_api_test import BaseAPITest


@allure.suite("Auth Service")
@allure.sub_suite("POST /auth/register")
class TestRegisterMethod(BaseAPITest):
    @allure.title("Validate registration")
    async def test_register_method(self, auth_service):
        with allure.step("Register"):
            response = await auth_service.register(
                body=RegisterRequest().model_dump()
            )
            self.assert_model(response, RegisterResponse)
