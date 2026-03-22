from src.app.models import (
    JobApplicationModel,
    CVModel,
    UserModel,
    CandidateAccountModel
)
from src.app.schemas.create_candidate_account_schemas import CreateCandidateAccountResponse
from src.app.schemas.create_cv_schemas import CreateCVResponse
from src.app.schemas.create_job_application_schemas import CreateJobApplicationResponse
from src.app.schemas.get_all_vancancies_schemas import (
    GetAllVacanciesResponse,
    Vacancy
)
from src.app.schemas.get_cvs_schemas import (
    GetCVsResponse,
    CVdata
)
from src.app.schemas.get_full_candidate_account_info_schemas import (
    GetFullCandidateAccountInfo,
    CV
)


class CandidateAccountServiceMapper:
    @staticmethod
    def all_vacancies(vacancies: dict):
        return GetAllVacanciesResponse(
            data=[
                Vacancy(
                    id=vacancy['id'],
                    job_title=vacancy['job_title'],
                    company_name=vacancy['company_name'],
                    min_salary=vacancy['min_salary'],
                    min_years_req=vacancy['min_years_req'],
                    job_location=vacancy['job_location']
                )
                for vacancy in vacancies
            ]
        )

    @staticmethod
    def created_application(created_application: JobApplicationModel):
        return CreateJobApplicationResponse(
            id=created_application.id,
            cv_id=created_application.cv_id,
            vacancy_id=created_application.vacancy_id,
            cover_letter=created_application.cover_letter
        )

    @staticmethod
    def all_cvs(cvs_info: list[CVdata]):
        return GetCVsResponse(
            data=cvs_info
        )

    @staticmethod
    def full_candidate_info(
            user: UserModel,
            candidate_account: CandidateAccountModel,
            cvs: list[CVModel]
    ):
        return GetFullCandidateAccountInfo(
            user_id=user.id,
            name=user.name,
            candidate_account_id=candidate_account.id,
            registration_date=str(user.created_at),
            cvs=[
                CV(
                    id=cv.id,
                    title=cv.title,
                    last_update=str(cv.updated_at)
                )
                for cv in cvs
            ]
        )

    @staticmethod
    def created_cv(cv: CVModel):
        return CreateCVResponse(
            id=cv.id,
            title=cv.title,
            content=cv.content
        )

    @staticmethod
    def created_candidate_account(candidate: CandidateAccountModel):
        return CreateCandidateAccountResponse(
            id=candidate.id,
            user_id=candidate.user_id
        )
