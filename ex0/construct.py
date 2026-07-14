import os
import site
import sys


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    activated = os.environ.get("VIRTUAL_ENV")
    source = activated if activated else sys.prefix
    return os.path.basename(source.rstrip(os.sep))


def get_site_packages() -> str:
    try:
        paths = site.getsitepackages()
    except (AttributeError, IndexError):
        return "unknown"
    return paths[0] if paths else "unknown"


def get_inside() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(get_site_packages())


def get_outside() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def main() -> None:
    try:
        if is_virtual_env():
            get_inside()
        else:
            get_outside()
    except OSError as e:
        print(f"MATRIX ERROR: unable to read the environment ({e})")


if __name__ == "__main__":
    main()
