from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.config import settings
from api_v1 import router as router_v1
from core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/helthcheck")
def read_root():
    return {"Hello": "World"}
