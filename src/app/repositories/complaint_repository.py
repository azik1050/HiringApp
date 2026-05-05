from sqlalchemy import select

from src.app.models import ComplaintModel, UserModel
from src.app.repositories._base_repository import BaseRepository
from src.app.schemas.create_complaint_schemas import CreateComplaintRequest


class ComplaintRepository(BaseRepository):
    async def get_all_with_user(self) -> list[tuple[ComplaintModel, UserModel]]:
        query = (
            select(ComplaintModel, UserModel)
            .join(UserModel, UserModel.id == ComplaintModel.user_id)
            .order_by(ComplaintModel.id.desc())
        )
        result = await self._session.execute(query)
        return result.all()

    async def create(self, user_id: int, complaint: CreateComplaintRequest) -> ComplaintModel:
        """
        Creates a new complaint in the database
        :param user_id: ID of the user who created the complaint
        :param complaint: Complaint data (CreateComplaintRequest)
        :return: Created complaint model
        """
        new_complaint = ComplaintModel(
            message=complaint.message,
            user_id=user_id
        )
        return await self._add(new_complaint)
