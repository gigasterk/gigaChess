from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.bd import db
from .schemas import RegisterSchema, LoginSchema
from .models import UserModel


@db.connection
async def create_user(user: RegisterSchema, session: AsyncSession) -> None:
    us = UserModel(**user.model_dump())

    session.add(us)
    await session.commit()


@db.connection
async def get_user(session: AsyncSession):
    query = select(UserModel)
    result = await session.execute(query)
    records = result.scalars().all()

    return records