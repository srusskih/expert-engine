from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GetPasswordSchemas(BaseModel):
    length: int   #  TODO: Add validation 1, 16
    use_special_characters: bool  # TODO: make int or boolean???
    use_numbers: bool
    use_capital_letters: bool


class NewPasswordSchemas(BaseModel):
    password: str


@app.get(
    "/get-password/",
    response_model=NewPasswordSchemas
)
def get_password(request: GetPasswordSchemas):
    return {"password": "password"}


class IsUsedPasswordSchemas(BaseModel):
    password: str


class IsUsedResponseSchemas(BaseModel):
    is_used: bool


@app.post(
    "/is-used-password/",
    response_model=IsUsedResponseSchemas
)
def is_used_password(request: IsUsedPasswordSchemas):
    return {"is_used": False}
