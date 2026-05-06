from typing import Optional
from sqlalchemy import select
from src.app.models.invitation_model import InvitationModel
from src.app.repositories._base_repository import BaseRepository
from src.app.schemas.create_invitation_schemas import CreateInvitationRequest


class InvitationRepository(BaseRepository):
    async def create_invitation(
            self,
            invitation: CreateInvitationRequest,
            vacancy_id: int
    ) -> InvitationModel:
        invitation = InvitationModel(
            message=invitation.message,
            job_application_id=invitation.job_application_id,
            vacancy_id=vacancy_id
        )

        return await self._add(invitation)

    async def get_invitation_by_application_id(self, application_id: int) -> Optional[InvitationRepository]:
        query = (
            select(InvitationModel)
            .where(InvitationModel.job_application_id == application_id)
        )
        result = await self._session.execute(query)
        return result.scalars().one_or_none()
