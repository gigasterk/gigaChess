from sqlalchemy.orm import sessionmaker

from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class DB:
    def __init__(self,
                 DB_HOST=settings.DB_HOST,
                 DB_PORT=settings.DB_PORT,
                 DB_USER=settings.DB_USER,
                 DB_PASSWORD=settings.DB_PASSWORD,
                 DB_NAME=settings.DB_NAME,
                 ):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD
        self.DB_NAME = DB_NAME

        self.engine = create_async_engine(url=self.get_db_url())
        self.sessionmaker = async_sessionmaker(bind=self.engine)


    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

db = DB()