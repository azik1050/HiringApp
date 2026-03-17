from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from authx import AuthXConfig

ENV_PATH = (Path().parent.parent.parent.parent / '.env').resolve()


class DevAuthConfig(BaseSettings):
    """Auth config"""
    jwt_secret_key: SecretStr
    jwt_access_token_expires: int = Field(default=3600)

    model_config = SettingsConfigDict(
        env_prefix="AUTH_",
        env_file=ENV_PATH,
        extra="ignore"
    )

    def create_authx_config(self):
        config = AuthXConfig(
            JWT_SECRET_KEY=self.jwt_secret_key.get_secret_value(),
            JWT_ACCESS_TOKEN_EXPIRES=self.jwt_access_token_expires
        )

        return config


class DevDBConfig(BaseSettings):
    """Database connection config"""
    name: str
    username: str
    password: SecretStr
    host: str
    port: int

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_prefix="DB_",
        extra="ignore"
    )


class AppConfig(BaseSettings):
    base_url: str

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_prefix="APP_",
        extra="ignore"
    )