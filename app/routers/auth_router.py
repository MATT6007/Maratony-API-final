from schemas.token_schema import Token
from fastapi.security import OAuth2PasswordRequestForm
from services.runner_services import RunnerService
from utils.auth_utils import create_access_token, authenticate_user, get_password_hash
from fastapi import APIRouter, Depends, status, HTTPException
from schemas.runners_schema import RunnerCreateRequest
from schemas.runners_schema import Runner as RunnerSchema
from models.runner import Runner
from dependencies.auth import get_current_active_user

import secrets
from datetime import timedelta
from config.settings import settings


router = APIRouter(tags=["Auth"])

@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        user_service: RunnerService = Depends()
):
    user = user_service.get_user_by_email(form_data.username)
    print(form_data.username)
    print(user)
    user = authenticate_user(user, form_data.password)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: RunnerCreateRequest,
                  runner_service: RunnerService = Depends()) -> RunnerSchema:
    user = runner_service.get_user_by_email(user_data.email)
    if user:
        raise HTTPException(status_code=400, detail="User with given email already exists")
    runner = Runner(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        date_of_birth=user_data.date_of_birth,
        email=user_data.email,
        phone=user_data.phone,
        image_url=user_data.image_url,
        password=get_password_hash(user_data.password),
        club=user_data.club
    )
    created_runner = runner_service.save(runner)
    return created_runner

@router.get("/users/me", response_model=RunnerSchema)
async def read_users_me(
        current_runner: Runner = Depends(get_current_active_user)
):
    return current_runner