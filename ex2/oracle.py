from __future__ import annotations
import os
from dotenv import load_dotenv

ENV_DEFAULTS = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "debug",
    "DATABASE_URL": "",
    "API_KEY": "",
    "ZION_ENDPOINT": "",
    }

def get_env() -> bool:
    print("This is what the shell + .env (in this order)contains")
    for name in ENV_DEFAULTS:
        env = os.getenv(name)
        print(name, repr(env))


def load_config() -> dict[str, str]:
    print("This is what the shell + .env + defaults (in this order) contains")
    defaults: dict[str,str] = {}
    for name, default in ENV_DEFAULTS.items():
        defaults[name] = os.getenv(name) or default
    return defaults


def validate_config(config: dict[str, str]) -> list[str]:
    missing: list[str] = []
    for key, value in config.items():
        if not value:
            missing.append(key)
    return missing


def display_config() -> None:
    ...


def security_check() -> None:
    ...


def main() -> None:
    loaded = load_dotenv()
    get_env()
    config = load_config()
    print(config)
    missing = validate_config(config)
    if missing:
        print("Missing in the configuration :")
        print(missing)


if __name__ == "__main__":
    main()
