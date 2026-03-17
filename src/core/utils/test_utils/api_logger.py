from httpx import Response
import allure
import json


class APILogger:
    @staticmethod
    async def save_allure(response: Response):
        endpoint = f"{response.request.method} {response.request.url}"
        # headers = f"{json.dumps(response.request.headers.raw, indent=4)}"
        body = f"{json.dumps(response.request.content, indent=4)}"

        allure.attach(
            body=endpoint,
            name="Endpoint",
            attachment_type=allure.attachment_type.TEXT
        )
        # allure.attach(
        #     body=headers,
        #     name="Headers",
        #     attachment_type=allure.attachment_type.TEXT
        # )
        allure.attach(
            body=body,
            name="Body",
            attachment_type=allure.attachment_type.JSON
        )