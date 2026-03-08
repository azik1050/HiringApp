from sqlalchemy.ext.asyncio import AsyncSession


class CandidateAccountRepository:
    @staticmethod
    async def create_candidate_account(
            candidate,
            db: AsyncSession
    ):
        pass
