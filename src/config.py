from functools import lru_cache
from pydantic import BaseSettings, Field
from pathlib import Path
import pathlib

class Settings(BaseSettings):
    DEBUG: bool = Field(..., env='DEBUG')
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    BASE_DIR: Path = pathlib.Path(__file__).parent
    STATIC_DIR: Path = BASE_DIR / 'static'
    TEMPLATES_DIR: Path = BASE_DIR / 'templates'
    STATIC_URL : str = '/static/'

    class Config:
        env_file = '.env'

@lru_cache
def get_settings():
    return Settings()