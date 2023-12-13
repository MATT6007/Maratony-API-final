# from services.user_service import UserService
from functools import wraps

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from services.runner_services import RunnerService
from models.runner import Runner
from config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# async def get_current_user(token: str = Depends(oauth2_scheme),
#                            user_service: RunnerService = Depends()):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = user_service.get_user_by_email(email)
#     if user is None:
#         raise credentials_exception
#     return user

async def get_current_user(token: str = Depends(oauth2_scheme),
                           user_service: RunnerService = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = user_service.get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Runner = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user