from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from src.core.config.settings import DevDBConfig


class Base(DeclarativeBase):
    pass


config = DevDBConfig()


DATABASE_URL = f"postgresql+asyncpg://{config.username}:{config.password.get_secret_value()}@{config.host}/{config.name}"


class DataBase:
    engine = create_async_engine(DATABASE_URL, echo=True)
    local_session = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    @classmethod
    async def setup_db(cls):
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def get_db(cls):
        async with cls.local_session() as session:
            yield session
