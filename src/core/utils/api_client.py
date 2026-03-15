from http import HTTPMethod
from typing import Optional
from httpx import Client


class APIClient:
    """Wrapper-class for sending external API requests"""
    def __init__(self, base_url: str):
        self._client = Client(
            base_url=base_url,
            timeout=100.0
        )

    def _request(
            self,
            method: HTTPMethod,
            endpoint: str,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            body: Optional[dict] = None,
            need_logging: bool = False
    ):
        """Method sending and logging HTTP request"""
        response = self._client.request(
            method=method,
            url=endpoint,
            headers=headers,
            params=params,
            json=body
        )

        if need_logging:
            """ Логгирование """
            ...

        return response

    def get(
            self,
            endpoint: str,
            *,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            need_logging: bool = False
    ):
        """Method for sending GET request"""
        return self._request(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            headers=headers,
            params=params,
            need_logging=need_logging
        )

    def post(
            self,
            endpoint: str,
            body: Optional[dict],
            *,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            need_logging: bool = False
    ):
        """Method for sending POST request"""
        return self._request(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            headers=headers,
            params=params,
            body=body,
            need_logging=need_logging
        )
