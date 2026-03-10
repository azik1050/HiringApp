from fastapi import HTTPException
from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, MappingResult
from src.app.models.company_account_model import CompanyAccountModel
from src.app.schemas.company_account_schemas import CreateCompanyAccountRequest


class CompanyAccountRepository:
    @staticmethod
    async def get_company_id_by_user_id(
            user_id: int,
            db: AsyncSession
    ) -> Optional[MappingResult]:
        query = (
            select(
                CompanyAccountModel.id.label("company_id")
            )
            .where(
                CompanyAccountModel.owner_id == user_id
            )
        )

        result = await db.execute(query)

        return result.mappings().one_or_none()

    @staticmethod
    async def create_company_account(
            user_id: int,
            company: CreateCompanyAccountRequest,
            db: AsyncSession
    ) -> CompanyAccountModel:
        new_company = CompanyAccountModel(
            name=company.name,
            short_description=company.short_description,
            long_description=company.long_description,
            owner_id=user_id
        )

        db.add(new_company)
        await db.commit()
        await db.refresh(new_company)

        return new_company