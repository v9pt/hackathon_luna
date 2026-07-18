from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    gemini_api_key: str
    gemini_model_name: str = "gemini-2.5-flash"
    max_cost_usd: float = 1.0
    max_iterations: int = 25

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Return cached Settings singleton. Call cache_clear() to reload."""
    return Settings()
