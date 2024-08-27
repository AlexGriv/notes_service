# app/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Сервис заметок'
    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()
