from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import Integer, func, String


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'


class UserModel(Base):
    username: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(String, unique=True)
    age: Mapped[int | None]
    rank: Mapped[int] = mapped_column(Integer, default=0)
    avatar: Mapped[str | None] = mapped_column(String, unique=True)
    achievements: Mapped[str | None] = mapped_column(String, default='Gamer')
    game_history: Mapped[str | None] = mapped_column(String, default='1')