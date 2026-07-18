import pytest

from app.config import get_settings


class TestSettings:
    """Tests for config.Settings loaded from environment."""

    def test_settings_loaded_from_env(self, monkeypatch: pytest.MonkeyPatch) -> None:
        get_settings.cache_clear()
        monkeypatch.setenv("GEMINI_API_KEY", "test-key-123")
        settings = get_settings()
        assert settings.gemini_api_key == "test-key-123"

    def test_settings_missing_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        get_settings.cache_clear()
        monkeypatch.delenv("GEMINI_API_KEY", raising=False)
        with pytest.raises(Exception):
            get_settings()
