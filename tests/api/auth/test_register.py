import allure
from src.app.schemas.auth_schemas import (
    RegisterRequest,
    RegisterResponse
)
import pytest


@allure.parent_suite("Internal Service API")
@allure.suite("Auth Service")
@allure.sub_suite("POST /auth/register")
@allure.title("Validate registration")
@pytest.mark.anyio
@pytest.mark.api
async def test_register_method(auth_service):
    with allure.step("Register"):
        response = await auth_service.register(
            body=RegisterRequest().model_dump()
        )
        assert response.status_code == 200
        RegisterResponse.model_validate(response.json())
