from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    batch_size: int = Field(..., env="batch_size")
    learning_rate: float = Field(..., env="learning_rate")
    epochs: int = Field(..., env="epochs")


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
print(settings)
