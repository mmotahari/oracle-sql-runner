from pathlib import Path

import yaml
from pydantic import BaseModel, SecretStr


BASE_DIR = Path(__file__).resolve().parents[2]
CONFIG_FILE = BASE_DIR / "config" / "database.yaml"


class OracleSettings(BaseModel):
    host: str
    port: int
    service_name: str
    username: str
    password: SecretStr


class DatabaseSettings(BaseModel):
    oracle: OracleSettings


def load_database_settings() -> DatabaseSettings:
    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    if not isinstance(config_data, dict):
        raise ValueError("Database configuration must be a YAML mapping")

    return DatabaseSettings(**config_data)


database_settings = load_database_settings()