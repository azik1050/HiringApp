from src.app.models import ComplaintModel, UserModel
from src.app.schemas.get_complaints_schemas import GetComplaintsResponse, Complaint, User


class AdminServiceMapper:
    @staticmethod
    def complaint_with_user(complaints_with_user: tuple[ComplaintModel, UserModel]):
        return GetComplaintsResponse(
            total=len(complaints_with_user),
            complaints=[
                Complaint(
                    user=User(id=user.id, username=user.name),
                    message=complaint.message
                )
                for complaint, user in complaints_with_user
            ],
        )

