from sqlalchemy.ext.asyncio import AsyncSession
from src.app.models.user_model import UserModel
from src.app.schemas.user_schemas import CreateUserRequest, CreateUserResponse


class UserRepository:
    @staticmethod
    async def create_user(
            user: CreateUserRequest,
            db: AsyncSession
    ) -> CreateUserResponse:
        user = UserModel(
            name=user.name
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return CreateUserResponse(
            id=user.id,
            name=user.name
        )

