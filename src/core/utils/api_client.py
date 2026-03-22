from http import HTTPMethod, HTTPStatus
from typing import Optional, Any
from httpx import AsyncClient, AsyncBaseTransport

from src.core.utils.test_utils.api_logger import APILogger


class APIClient:
    """Wrapper-class for sending external API requests"""

    def __init__(
            self,
            base_url: str,
            timeout: float = 100.0,
            follow_redirects: bool = True,
            transport: Optional[AsyncBaseTransport] = None
    ):
        self._client = AsyncClient(
            base_url=base_url,
            timeout=timeout,
            follow_redirects=follow_redirects,
            transport=transport
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self._client.is_closed:
            await self._client.aclose()

    async def _request(
            self,
            method: HTTPMethod,
            endpoint: str,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            body: Optional[dict] = None,
            need_logging: bool = False,
            expected_status: Optional[HTTPStatus] = None
    ):
        """Method sending and logging HTTP request"""
        response = await self._client.request(
            method=method,
            url=endpoint,
            headers=headers,
            params=params,
            json=body
        )

        if need_logging:
            await APILogger.save_allure(response)

        if expected_status:
            assert expected_status.value == response.status_code, (
                f"Invalid response received for {response.request.url}",
                f"Code: {response.status_code}. Body: {response.content}"
            )

        return response

    async def set_header(self, key: str, value: Any):
        self._client.headers.update({key: value})

    async def get(
            self,
            endpoint: str,
            *,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            need_logging: bool = False,
            expected_status: Optional[HTTPStatus] = None
    ):
        """Method for sending GET request"""
        return await self._request(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            headers=headers,
            params=params,
            need_logging=need_logging,
            expected_status=expected_status
        )

    async def post(
            self,
            endpoint: str,
            body: Optional[dict] = None,
            *,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            need_logging: bool = False,
            expected_status: Optional[HTTPStatus] = None
    ):
        """Method for sending POST request"""
        return await self._request(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            headers=headers,
            params=params,
            body=body,
            need_logging=need_logging,
            expected_status=expected_status
        )
