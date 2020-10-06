from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.lists.endpoints import router as list_router
from app.api.items.endpoints import router as item_router

from mangum import Mangum

import os

if os.environ.get("API_PREFIX", None):
    app = FastAPI(openapi_prefix=os.environ.get("API_PREFIX"))
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(list_router, prefix="/lists")
app.include_router(item_router, prefix="/items")

handler = Mangum(app)