from abc import ABC
from typing import Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Select, delete, MappingResult


class BaseRepository(ABC):
    """Abstract class providing methods for general db interaction"""
    def __init__(self, session: AsyncSession):
        self._session = session

    async def _find_all(self, query: Select[Any]) -> list[Any]:
        """
        Returns all models found in DB as a list
        :parameter query: SQL select query
        :return: list of DB models
        """
        result = await self._session.execute(query)

        return [model for model in result.scalars().all()]

    async def _find_one(self, query: Select[Any]) -> Optional[DeclarativeBase]:
        """
        Returns all models found in DB as a list
        :parameter query: SQL select query
        :return: DB models as a list
        """
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def _find_one_labeled(self, query: Select[Any]) -> Optional[MappingResult]:
        """
        Returns one model found in DB as a list
        :parameter query: SQL select query
        :return: DB model (if found) or null
        """
        result = await self._session.execute(query)
        return result.mappings().one_or_none()


    async def _add(self, model: DeclarativeBase) -> Any:
        """
        Inserts model into DB
        :param model: to be added to DB
        :return: model added to DB
        """
        self._session.add(model)
        await self._session.commit()
        await self._session.refresh(model)

        return model

    async def _delete(self, model: DeclarativeBase, **condition):
        """
        Deletes chosen model from DB
        :param model: Model to be deleted
        :param condition: Condition for deletion
        :return:
        """
        query = (
            delete(model)
            .where(**condition)
        )
        await self._session.execute(query)
        await self._session.commit()
