import uvicorn
from fastapi import FastAPI
from src.app.routers import (
    user_router,
    candidate_router,
    company_router,
    auth_router
)
from src.core.auth.security import security
from src.core.database.database_helper import DataBase

app = FastAPI(
    on_startup=[
        DataBase.setup_db
    ]
)

# routers
app.include_router(user_router.router)
app.include_router(candidate_router.router)
app.include_router(company_router.router)
app.include_router(auth_router.router)

security.handle_errors(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# User

# CandidateAccount;
# CV; JobApplication;

# CompanyAccount;
# Vacancy; Invitation;

# Common:
# Statistics
# Complaint
