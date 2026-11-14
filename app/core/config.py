from pathlib import Path

import yaml
from pydantic import BaseModel


BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILE = BASE_DIR / "config" / "app.yaml"


class AppSettings(BaseModel):
    name: str
    version: str
    environment: str


class ServerSettings(BaseModel):
    host: str
    port: int


class Settings(BaseModel):
    app: AppSettings
    server: ServerSettings


def load_settings() -> Settings:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    if not isinstance(config_data, dict):
        raise ValueError("Application configuration must be a YAML mapping")

    return Settings(**config_data)


settings = load_settings()