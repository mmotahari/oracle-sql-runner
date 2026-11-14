from pathlib import Path

import yaml
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILE = BASE_DIR / "config" / "app.yaml"


class AppSettings(BaseModel):
    name: str
    version: str
    environment: str


class ServerSettings(BaseModel):
    host: str
    port: int


class SQLExecutionSettings(BaseModel):
    sqlcl_path: str
    timeout_seconds: int = Field(gt=0)


class Settings(BaseModel):
    app: AppSettings
    server: ServerSettings
    sql_execution: SQLExecutionSettings


def load_settings() -> Settings:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    if not isinstance(config_data, dict):
        raise ValueError("Application configuration must be a YAML mapping")

    return Settings(**config_data)


settings = load_settings()