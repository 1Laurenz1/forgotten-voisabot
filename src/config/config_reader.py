from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path


class Settings(BaseSettings):
    API_ID: SecretStr
    API_HASH: SecretStr
    
    BOT_USERNAME: str = "voisabot"
    
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="UTF-8",
        extra="forbid",
    )
    
    
settings = Settings()
