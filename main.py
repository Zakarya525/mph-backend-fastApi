from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.auth import auth_router
from api.product import product_router
from api.store import store_router
from api.user import user_router

app = FastAPI(title="Mardan Peera House")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(store_router)
app.include_router(product_router)
