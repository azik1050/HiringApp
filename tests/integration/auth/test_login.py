import allure
from src.app.schemas.auth_schemas import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse
)
from tests.integration.base_api_test import BaseAPITest


@allure.suite("Auth Service")
@allure.sub_suite("POST /auth/login")
class TestLoginMethod(BaseAPITest):
    @allure.title("Validate login")
    async def test_login_method(self, auth_service):
        register_request = RegisterRequest()
        with allure.step("Register"):
            response = await auth_service.register(
                body=register_request.model_dump()
            )
            self.assert_model(response, RegisterResponse)
        with allure.step("Login"):
            response = await auth_service.login(
                body=LoginRequest(
                    name=register_request.name,
                    password=register_request.password
                ).model_dump()
            )
            self.assert_model(response, LoginResponse)
