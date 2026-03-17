from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.core.config.settings import DevDBConfig


class Base(DeclarativeBase):
    pass


config = DevDBConfig()


# DATABASE_URL = URL.create(
#     drivername="postgresql+asyncpg",
#     username=config.username,
#     password=config.password.get_secret_value(),
#     host=config.host,
#     port=config.port,
#     database=config.name
# )
DATABASE_URL = f"postgresql+asyncpg://{config.username}:{config.password.get_secret_value()}@{config.host}/{config.name}"

class DataBase:
    engine = create_async_engine(DATABASE_URL, echo=True)

    @classmethod
    async def setup_db(cls):
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def get_db(cls):
        async with AsyncSession(bind=cls.engine) as session:
            yield session
