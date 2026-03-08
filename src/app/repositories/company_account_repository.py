from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models.company_account_model import CompanyAccountModel
from src.app.schemas.company_account_schemas import CreateCompanyAccountRequest


class CompanyAccountRepository:
    @staticmethod
    async def create_company_account(
            company: CreateCompanyAccountRequest,
            db: AsyncSession
    ) -> CompanyAccountModel:
        new_company = CompanyAccountModel(
            name=company.name,
            short_description=company.short_description,
            long_description=company.long_description,
            owner_id=company.owner_id
        )

        db.add(new_company)
        await db.commit()
        await db.refresh(new_company)

        return new_company