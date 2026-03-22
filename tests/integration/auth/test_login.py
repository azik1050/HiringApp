import allure
from src.app.schemas.auth_schemas import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse
)
from src.core.utils.data_generator import DataGenerator

from tests.integration.base_api_test import BaseAPITest


@allure.suite("Auth Service")
@allure.sub_suite("POST /auth/login")
class TestRegisterMethod(BaseAPITest):
    @allure.title("Validate login")
    async def test_register_method(self, auth_service):
        name, password = DataGenerator.name(), DataGenerator.password()
        with allure.step("Register"):
            response = await auth_service.register(
                body=RegisterRequest(
                    name=name,
                    password=password
                ).model_dump()
            )
            self.assert_model(response, RegisterResponse)
        with allure.step("Login"):
            response = await auth_service.login(
                body=LoginRequest(
                    name=name,
                    password=password
                ).model_dump()
            )
            self.assert_model(response, LoginResponse)
