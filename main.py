from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI, status

from core.config import settings
from api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/helthcheck", status_code=status.HTTP_200_OK)
def helthcheck():
    return {"App": "is helthy"}


@app.get("/")
def home():
    return {"Hello": "App is ready to work"}
