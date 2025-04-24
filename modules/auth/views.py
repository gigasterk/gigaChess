from fastapi import APIRouter
from .schemas import RegisterSchema, LoginSchema
from .crud import create_user as create_user_crud, get_user

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get("/sign")
async def sign():
    return {"message": f"sign page with login register google yandex login"}

@router.post("/register")
async def create_user(user: RegisterSchema):
    await create_user_crud(user)
    return {"message": f"user created successfully"}

@router.get("/get_users")
async def get_users():
    us = await get_user()
    return {"users": us}

@router.post("/login")
async def login(user: LoginSchema):
    pass