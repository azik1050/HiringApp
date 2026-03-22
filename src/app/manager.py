import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.app.routers import (
    user_router,
    candidate_router,
    company_router,
    auth_router
)
from src.core.auth.security import security
from src.core.config.settings import AppConfig
from src.core.database.database_helper import DataBase

config = AppConfig()


def create_app():
    app = FastAPI(
        # on_startup=[
        #     DataBase.setup_db
        # ]
    )

    app.include_router(user_router.router)
    app.include_router(candidate_router.router)
    app.include_router(company_router.router)
    app.include_router(auth_router.router)

    security.handle_errors(app)

    app.add_middleware(CORSMiddleware, allow_origins=['*'])

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="127.0.0.1", port=8000)
