# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str = "development"
    debug: bool = True
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "change-me"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()