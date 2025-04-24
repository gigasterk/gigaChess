from fastapi import APIRouter
from .schemas import User
from .crud import create_user as create_user_crud

router = APIRouter(prefix='/auth')

@router.get("/sign")
async def sign():
    return {"message": f"sign page with login register google yandex login"}

@router.post("/signup")
async def create_user(user: User):
    await create_user_crud(user)
    return {"message": f"user created successfully"}

@router.post("/login")
async def login():
    pass