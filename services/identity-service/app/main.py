from fastapi import FastAPI

from app.api.health import router

app = FastAPI(title="Identity Service")

app.include_router(router)
