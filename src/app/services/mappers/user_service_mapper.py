from src.app.models import UserModel
from src.app.schemas.create_user_schemas import (
    GetUserResponse,
    GetUsersResponse,
    User,
    CreateUserResponse
)


class UserServiceMapper:
    @staticmethod
    def user_info(user_info: dict):
        return GetUserResponse(
            id=user_info['id'],
            name=user_info['name'],
            candidate_account_id=user_info['candidate_account_id'],
            company_account_id=user_info['company_account_id']
        )

    @staticmethod
    def users_all(users: list[UserModel]):
        return GetUsersResponse(
            data=[
                User(
                    id=user.id,
                    name=user.name
                )
                for user in users
            ]
        )

    @staticmethod
    def created_user(user: UserModel):
        return CreateUserResponse(
            id=user.id,
            name=user.name
        )