from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    gemini_api_key: str
    gemini_model_name: str = "gemini-2.0-flash"
    max_cost_usd: float = 1.0
    max_iterations: int = 8
    # Delay (seconds) between Gemini API calls to respect free-tier rate limits.
    # Free tier: 5 req/min → set to 13s.  Paid tier: set to 0.
    gemini_request_delay: float = 13.0

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Return cached Settings singleton. Call cache_clear() to reload."""
    return Settings()
