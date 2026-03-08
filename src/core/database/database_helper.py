from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


class DataBase:
    engine = create_async_engine("sqlite+aiosqlite://", echo=True)
    async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

    @classmethod
    async def setup_db(cls):
        async with cls.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    async def get_db(cls):
        async with AsyncSession(bind=cls.engine) as session:
            yield session
