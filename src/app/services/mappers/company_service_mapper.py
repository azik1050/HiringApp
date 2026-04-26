from src.app.models import (
    CompanyAccountModel,
    VacancyModel, InvitationModel
)
from src.app.schemas.create_company_account_schemas import CreateCompanyAccountResponse
from src.app.schemas.create_invitation_schemas import CreateInvitationResponse
from src.app.schemas.create_vacancy_schemas import CreateVacancyResponse
from src.app.schemas.get_company_info import (
    GetCompanyInfoResponse,
    Vacancy
)
from src.app.schemas.get_company_vacancy_by_id import (
    VacancyApplication,
    GetCompanyVacancyByIdResponse
)


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
    def company_info(
            company: CompanyAccountModel,
            vacancies: list[VacancyModel]
    ):
        return GetCompanyInfoResponse(
            id=company.id,
            name=company.name,
            short_description=company.short_description,
            full_description=company.long_description,
            vacancies=[
                Vacancy(
                    id=vacancy.id,
                    title=vacancy.title,
                    description=vacancy.description,
                    last_update_date=str(vacancy.last_update_date)
                )
                for vacancy in vacancies
            ]
        )

    @staticmethod
    def company_vacancy(
            vacancy: VacancyModel,
            applications_info: dict
    ):
        return GetCompanyVacancyByIdResponse(
            id=vacancy.id,
            title=vacancy.title,
            description=vacancy.description,
            minimal_salary=vacancy.minimal_salary,
            minimal_year_exp=vacancy.minimal_year_exp,
            job_location=vacancy.job_location,
            creation_date=str(vacancy.creation_date),
            last_update_date=str(vacancy.last_update_date),
            applications=[
                VacancyApplication(
                    id=app['id'],
                    candidate_name=app['candidate_name'],
                    accepted=app['accepted'],
                    cover_letter=app['cover_letter'],
                    created_at=str(app['created_at'])
                )
                for app in applications_info
            ]
        )

    @staticmethod
    def created_invitation(
            invitation: InvitationModel
    ):
        return CreateInvitationResponse(
            id=invitation.id,
            message=invitation.message,
            job_application_id=invitation.job_application_id
        )