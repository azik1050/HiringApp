from src.app.repositories.complaint_repository import ComplaintRepository
from src.app.services.mappers.admin_service_mapper import AdminServiceMapper


class AdminService:
    def __init__(self, complaint_repository: ComplaintRepository):
        self.complaint_repository = complaint_repository
        self.mapper = AdminServiceMapper()

    async def show_complaints(self):
        complaints = await self.complaint_repository.get_all_with_user()
        return self.mapper.complaint_with_user(complaints)





