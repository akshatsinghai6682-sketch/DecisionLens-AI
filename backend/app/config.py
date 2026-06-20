"""Configuration management for DecisionLens AI backend"""

from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # API
    API_TITLE: str = "DecisionLens AI"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "AI-powered life decision simulator and second-opinion reasoning system"

    # Server
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost/decisionlens"
    )
    DATABASE_ECHO: bool = DEBUG
    DATABASE_POOL_SIZE: int = 5
    DATABASE_MAX_OVERFLOW: int = 10

    # Gemini API
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = "gemini-pro"
    MAX_TOKENS: int = 2000
    TEMPERATURE: float = 0.7

    # AI Parameters
    NUM_SCENARIOS: int = 3
    NUM_TRADEOFFS: int = 5
    NUM_DIAGNOSTIC_QUESTIONS: int = 5
    NUM_ADVISORS: int = 5
    CONFIDENCE_THRESHOLD: float = 0.7

    # PDF Settings
    PDF_PAGE_WIDTH: int = 8.5
    PDF_PAGE_HEIGHT: int = 11.0
    PDF_MARGIN: int = 0.5

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
