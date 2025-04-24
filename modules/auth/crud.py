from sqlalchemy.ext.asyncio import AsyncSession
from core.bd import db
from .schemas import User
from .models import UserModel


async def create_user(user: User) -> None:
    us = UserModel(**user.model_dump())

    sesion = AsyncSession(db.engine)
    sesion.add(us)
    await sesion.commit()