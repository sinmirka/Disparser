from pathlib import Path
from shutil import copytree, rmtree

from utils.paths import PROFILES_DIR

def prepare_profile(profile: Path) -> Path:
    if not profile.exists():
        raise FileNotFoundError("Profile not found")
    
    destination = PROFILES_DIR / profile.name
    
    if destination.exists():
        rmtree(destination)

    copytree(src=profile, dst=destination)

