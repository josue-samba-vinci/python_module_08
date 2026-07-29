from __future__ import annotations
import os
import sys
from dotenv import load_dotenv, find_dotenv

ENV_DEFAULTS = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "INFO",
    "DATABASE_URL": "",
    "API_KEY": "",
    "ZION_ENDPOINT": "",
    }
SECRET_VARS = {"API_KEY", "DATABASE_URL"}

VALID_MODES = {"development", "production"}


def load_config() -> dict[str, str]:
    config: dict[str, str] = {}
    for name, default in ENV_DEFAULTS.items():
        config[name] = os.getenv(name) or default
    config["MATRIX_MODE"] = config["MATRIX_MODE"].strip().lower()
    return config


def validate_config(config: dict[str, str]) -> list[str]:
    missing: list[str] = []
    for key, value in config.items():
        if not value:
            missing.append(key)
    return missing


def display_config(config: dict[str, str]) -> None:
    matrix_mode = config["MATRIX_MODE"]
    log_level = config["LOG_LEVEL"]
    api_key = config["API_KEY"]
    zion_endpoint = config["ZION_ENDPOINT"]
    print()
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    database = "Connected to local instance"
    if matrix_mode == "production":
        database = "Connected to production instance"
    print(f"Database: {database}")
    print(f"API Access: {'Authenticated' if api_key else 'Not configured'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Offline'}")


def security_check(loaded: bool, before: dict[str, str]) -> None:
    print()
    print("Environment security check:")
    ok = True
    for key, default in ENV_DEFAULTS.items():
        if key in SECRET_VARS and default:
            ok = False
    if ok:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Hardcoded secrets detected")
    if find_dotenv() and loaded:
        print("[OK] .env file properly configured")
    elif find_dotenv() and not loaded:
        print("[KO] .env file is empty")
        print("fill it by placing informations inside every field", end="")
        print(" in the .env.example and then by using : cp .env.example .env")
    else:
        print("[KO] .env file doesn't exist")
        print("create it by placing informations inside every field in")
        print("the .env.example and then by using : cp .env.example .env")
    ok = True
    for name in ENV_DEFAULTS:
        if name in before and os.getenv(name) != before[name]:
            ok = False
    if ok:
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides not available")
        print("Please don't modify the load_dotenv() method")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    before = dict(os.environ)
    loaded = load_dotenv()
    config = load_config()
    if config["MATRIX_MODE"] not in VALID_MODES:
        print("the matrix_mode is either 'production' or 'development'",
              file=sys.stderr)
        print(
            "it will now be set automatically to "
            "'development' for safety reasons", file=sys.stderr)
        config["MATRIX_MODE"] = "development"
    missing = validate_config(config)
    if missing:
        if config["MATRIX_MODE"] == "production":
            print(
                "WARNING : You're inside the production !!!!", file=sys.stderr
                )
            print(missing, file=sys.stderr)
            sys.exit(1)
        else:
            print("Missing in the configuration :")
            print(missing)
    display_config(config)
    security_check(loaded, before)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
