from typing import Optional

from httpx import Response
import allure
import json


class APILogger:
    @staticmethod
    async def save_allure(response: Response):
        # Save request
        endpoint = f"{response.request.method} {response.request.url}\n"

        headers: str = "Headers:\n"
        for key, val in response.request.headers.items():
            headers += f"  {key}: {val}\n"

        if response.request.read():
            body = "Body:\n" + json.dumps(
                json.loads(response.request.content),
                indent=2
            )
        else:
            body = "Body: None"

        allure.attach(
            body=endpoint + headers + body,
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

        # Save response
        status_code = "Status code: " + str(response.status_code)

        if response.content:
            response_body = "\nResponse json: " + json.dumps(
                response.json(),
                indent=2
            )
        else:
            response_body = "\nResponse json: None"
        allure.attach(
            body=status_code + response_body,
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )
