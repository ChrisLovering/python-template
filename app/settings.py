import pydantic_settings


class _Settings(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    debug: bool = False
    git_sha: str = "development"


SETTINGS: _Settings = _Settings()
