from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "BakChek"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    MODEL_PATH: str = "app/ml/models/model.pkl"
    
    class Config:
        env_file = ".env"

settings = Settings()