from sqlalchemy.ext.asyncio import AsyncSession
from src.app.repositories.user_repository import UserRepository
from src.app.schemas.user_schemas import CreateUserRequest


class UserService:
    async def create_user(
            self,
            user: CreateUserRequest,
            db: AsyncSession
    ):
        created_user = await UserRepository.create_user(user, db)
        return created_user
