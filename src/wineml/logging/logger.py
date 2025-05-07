# src/wineml/logging/logger.py

import logging
import os

logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE = os.path.join(logs_dir, "running_logs.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("wineml")
logger.setLevel(logging.INFO)

# Also log to terminal
if not logger.handlers:
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s: %(levelname)s]: %(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

__all__ = ["logger"]
