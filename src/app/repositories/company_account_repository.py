from typing import Optional
from sqlalchemy import select, MappingResult
from src.app.models.company_account_model import CompanyAccountModel
from src.app.schemas.create_company_account_schemas import CreateCompanyAccountRequest
from src.core.base_classes.repository import BaseRepository


class CompanyAccountRepository(BaseRepository):
    async def get_company_id_by_user_id(
            self,
            user_id: int
    ) -> Optional[MappingResult]:
        query = (
            select(
                CompanyAccountModel.id.label("company_id")
            )
            .where(
                CompanyAccountModel.owner_id == user_id
            )
        )

        return await self._find_one_labeled(query)

    async def create_company_account(
            self,
            user_id: int,
            company: CreateCompanyAccountRequest
    ) -> CompanyAccountModel:
        new_company = CompanyAccountModel(
            name=company.name,
            short_description=company.short_description,
            long_description=company.long_description,
            owner_id=user_id
        )

        return await self._add(new_company)