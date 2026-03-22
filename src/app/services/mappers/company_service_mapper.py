from src.app.models import CompanyAccountModel
from src.app.schemas.create_company_account_schemas import CreateCompanyAccountResponse
from src.app.schemas.create_vacancy_schemas import CreateVacancyResponse
from src.app.schemas.get_vacancy_by_id_schemas import GetVacancyByIdResponse


class CompanyServiceMapper:
    @staticmethod
    def created_company(company: CompanyAccountModel):
        return CreateCompanyAccountResponse(
            id=company.id,
            name=company.name,
            short_description=company.short_description,
            long_description=company.long_description
        )

    @staticmethod
    def created_vacancy(vacancy):
        return CreateVacancyResponse(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            minimal_salary=vacancy.minimal_salary,
            minimal_year_exp=vacancy.minimal_year_exp,
            job_location=vacancy.job_location
        )

    @staticmethod
    def vacancy(vacancy):
        return GetVacancyByIdResponse(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            company_id=vacancy.company_id,
            minimal_salary=vacancy.minimal_salary,
            minimal_year_exp=vacancy.minimal_year_exp,
            job_location=vacancy.job_location,
            creation_date=str(vacancy.creation_date),
            last_update_date=str(vacancy.last_update_date)
        )
