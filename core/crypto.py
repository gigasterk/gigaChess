import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from config import settings


def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.PRIVATE_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def check_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)

def decode_username_from_token(token: str):
    payload = jwt.decode(token, settings.PUBLIC_KEY, algorithms=["RS256"])
    username = payload.get("sub")
    return username