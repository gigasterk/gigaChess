from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import InvalidTokenError
from starlette import status

from .schemas import RegisterSchema, LoginSchema, TokenSchema, User
from .crud import create_user as create_user_crud, check_user, user_includes
from core.crypto import create_access_token, decode_username_from_token
from config import settings
router = APIRouter(prefix='/auth', tags=['auth'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/sign")
async def sign():
    return {"message": f"sign page with login register google yandex login"}

@router.post("/register")
async def create_user(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> TokenSchema:
    user = RegisterSchema(
        username=form_data.username,
        email=form_data.password,
    )
    ac = await create_user_crud(user)
    if not ac:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username already registered!")

    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return TokenSchema(
        token_type="bearer",
        access_token=access_token
    )

@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> TokenSchema:
    user = LoginSchema(
        username=form_data.username,
        password=form_data.password,
    )
    ch = await check_user(user)
    if ch:
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        return TokenSchema(
            token_type="bearer",
            access_token=access_token
        )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        username = decode_username_from_token(token)
        if not username:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    if await user_includes(username=username):
        return User(username=username)

@router.get("/profile")
async def profile(
    current_user: Annotated[User, Depends(get_current_user)]
):
    return {'username': current_user.username, 'id': 0}