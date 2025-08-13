from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 5000
    TELEGRAM_API_ID: int
    TELEGRAM_API_HASH: str
    SESSIONS_DIR: str = "./sessions"
    MASTER_KEY: str = "change_me"

    model_config = SettingsConfigDict(env_file=Path(__file__).resolve().parents[1] / ".env", env_file_encoding="utf-8")


settings = Settings()
