import pathlib
from decouple import config
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = config("DEBUG", cast=bool)
    SECRET_KEY: str = config("SECRET_KEY", cast=str)
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent
    STATIC_DIR: pathlib.Path = BASE_DIR / "static"
    TEMPLATES_DIR: pathlib.Path = BASE_DIR / "templates"
    STATIC_URL: str = config("STATIC_URL", cast=str, default="/static/")


@lru_cache()
def get_settings():
    return Settings()
