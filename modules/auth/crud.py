from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core.bd import db
from .schemas import RegisterSchema, LoginSchema, User
from .models import UserModel
from core.crypto import check_password, hash_password


@db.connection
async def create_user(user: RegisterSchema, session: AsyncSession) -> bool:
    us = await session.execute(select(UserModel).where(UserModel.username == user.username))
    if us.scalar():
        return False
    to_database = user.model_dump()
    to_database['password'] = hash_password(to_database['password'])
    us = UserModel(**to_database)
    session.add(us)
    await session.commit()
    return True


@db.connection
async def check_user(user: LoginSchema, session: AsyncSession) -> bool:
    us = await session.execute(select(UserModel).where(UserModel.username == user.username))
    us = us.scalar()
    if not us:
        return False
    if not check_password(user.password, us.password):
        return False
    return True

@db.connection
async def user_includes(session: AsyncSession, username: str) -> bool:
    us = await session.execute(select(UserModel).where(UserModel.username == username))
    if us.scalar():
        return True
    return False