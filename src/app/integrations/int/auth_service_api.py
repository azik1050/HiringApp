from http import HTTPStatus
from typing import Optional

from src.core.utils.api_client import APIClient


class AuthServiceAPI:
    def __init__(self, api_client: APIClient):
        self._api_client = api_client

    async def register(
            self,
            body: Optional[dict] = None,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status: HTTPStatus = HTTPStatus.OK
    ):
        """ Send request to POST /auth/register """
        return await self._api_client.post(
            endpoint="/auth/register",
            body=body,
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )