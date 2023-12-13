from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from routers import address_router
from routers import competition_category_router
from routers import competition_router
from routers import sponsors_router
from routers import sponsors_competition_router
from routers import auth_router

from dependencies.database import Base, engine  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
app.include_router(address_router.router)
app.include_router(competition_category_router.router)
app.include_router(competition_router.router)
app.include_router(sponsors_router.router)
app.include_router(sponsors_competition_router.router) 

add_pagination(app)


