from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv(override=True)

class Settings(BaseSettings):
    DATABASE_URL: str
    STATSIG_API_KEY: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings() -> Settings:
    return Settings()