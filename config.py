from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class Setting(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    PRIVATE_KEY: str = open(BASE_DIR / 'key.pem').read()
    PUBLIC_KEY: str = open(BASE_DIR / 'public.pem').read()
    ALGORITHM: str = 'RS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Setting(_env_file='config.env')
