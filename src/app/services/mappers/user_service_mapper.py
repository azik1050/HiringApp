from src.app.models import UserModel, ComplaintModel
from src.app.schemas.create_user_schemas import (
    GetUserResponse,
    GetUsersResponse,
    User,
    CreateUserResponse
)
from src.app.schemas.create_complaint_schemas import CreateComplaintResponse


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

    @staticmethod
    def created_complaint(complaint: ComplaintModel) -> CreateComplaintResponse:
        """
        Maps a ComplaintModel to CreateComplaintResponse
        :param complaint: Created complaint model
        :return: CreateComplaintResponse
        """
        return CreateComplaintResponse(
            id=complaint.id,
            message=complaint.message,
            user_id=complaint.user_id
        )
