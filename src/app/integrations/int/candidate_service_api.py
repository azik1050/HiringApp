from http import HTTPStatus
from typing import Optional

from src.core.utils.api_client import APIClient


class CandidateServiceAPI:
    def __init__(self, api_client: APIClient):
        self._api_client = api_client

    async def create_candidate(
            self,
            body: Optional[dict] = None,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status: HTTPStatus = HTTPStatus.CREATED
    ):
        """ Send request to POST /candidate-account """
        return await self._api_client.post(
            endpoint="/candidate-account",
            body=body,
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )

    async def create_cv(
            self,
            body: Optional[dict] = None,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status: HTTPStatus = HTTPStatus.CREATED
    ):
        """ Send request to POST /candidate-account/cv """
        return await self._api_client.post(
            endpoint="/candidate-account/cv",
            body=body,
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )

    async def get_full_candidate_account_info(
            self,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status: HTTPStatus = HTTPStatus.OK
    ):
        """ Send request to GET /candidate-account/info """
        return await self._api_client.get(
            endpoint="/candidate-account/info",
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )

    async def get_candidate_account_cvs(
            self,
            headers: Optional[dict] = None,
            params: Optional[dict] = None,
            expected_status: HTTPStatus = HTTPStatus.OK
    ):
        """ Send request to GET /candidate-account/cv """
        return await self._api_client.get(
            endpoint="/candidate-account/cv/all",
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )
