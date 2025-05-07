# src/wineml/constants/__init__.py
from pathlib import Path

# 👇 This always gives you the actual project root, no matter where you're running from
ROOT_DIR = Path(__file__).resolve().parents[3]

# 👇 Now you can build any path safely relative to project root
CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "config" / "schema.yaml"  # optional