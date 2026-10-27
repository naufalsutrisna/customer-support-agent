
from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Customer Support Agent")

app.include_router(router)
