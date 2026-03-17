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
            endpoint="/candidate_account",
            body=body,
            headers=headers,
            params=params,
            expected_status=expected_status,
            need_logging=True
        )