from pathlib import Path
import os

LOCAL_APPDATA = Path(os.environ["LOCALAPPDATA"])

DISPARSER_DIR = LOCAL_APPDATA / "Disparser"
PROFILES_DIR = DISPARSER_DIR / "Profiles"
LOGS_DIR = DISPARSER_DIR / "Logs"