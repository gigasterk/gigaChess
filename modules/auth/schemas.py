from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(LoginSchema):
    email: str


class User(BaseModel):
    username: str


class TokenSchema(BaseModel):
    access_token: str
    token_type: str