import allure
import pytest
from httpx import Response
from pydantic import BaseModel


@allure.parent_suite("Internal Service API")
@pytest.mark.anyio
@pytest.mark.api
class BaseAPITest:
    def assert_status_code(
            self,
            response: Response,
            expected_code: int
    ):
        with allure.step("Check response code"):
            assert response.status_code == expected_code, (
                f"Response for {response.url} != {expected_code}"
            )

    def assert_model(
            self,
            response: Response,
            model: type[BaseModel]
    ):
        with allure.step("Check response model"):
            model.model_validate(response.json())
