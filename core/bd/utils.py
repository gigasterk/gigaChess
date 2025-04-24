from config import settings
from sqlalchemy.ext.asyncio import create_async_engine

class DB:
    def __init__(self,
                 url: str = settings.db_url,
                 echo: bool = settings.db_echo,
                 ):

        self.engine = create_async_engine(url=url,
                                          echo=echo)


db = DB()