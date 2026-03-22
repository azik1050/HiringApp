from src.app.models import UserModel
from src.app.schemas.auth_schemas import (
    RegisterResponse,
    LoginResponse
)


class AuthServiceMapper:
    @staticmethod
    def user(user: UserModel):
        return RegisterResponse(
            id=user.id,
            name=user.name
        )

    @staticmethod
    def auth_details(access_token: str):
        return LoginResponse(
            access_token=access_token
        )