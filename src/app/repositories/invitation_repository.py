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

