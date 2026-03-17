import pytest
from httpx import ASGITransport
from src.app.integrations.int.auth_service_api import AuthServiceAPI
from src.app.integrations.int.candidate_service_api import CandidateServiceAPI
from src.app.manager import create_app
from src.core.auth.security import security
from src.core.utils.api_client import APIClient


@pytest.fixture(scope="function")
async def int_api_client():
    async with APIClient(
            base_url="http://127.0.0.1:8000",
            transport=ASGITransport(app=create_app())
    ) as client:
        yield client


@pytest.fixture(scope="function")
async def auth_service(int_api_client):
    return AuthServiceAPI(int_api_client)


@pytest.fixture(scope="function")
async def candidate_service(int_api_client):
    return CandidateServiceAPI(int_api_client)


@pytest.fixture(scope="function", autouse=True)
async def auth_token_guard(int_api_client):
    access_token = security.create_access_token(uid="1")
    await int_api_client.set_header("Authorization", access_token)
