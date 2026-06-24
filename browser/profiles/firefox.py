from pathlib import Path
import configparser

def get_firefox_profile() -> Path:
    firefox_dir = (
        Path.home()
        / "AppData"
        / "Roaming"
        / "Mozilla"
        / "Firefox"
    )

    config = configparser.ConfigParser()
    config.read(firefox_dir / "profiles.ini")

    for section in config.sections(): # new method
        if section.startswith("Install"):
            return firefox_dir / config[section]["Default"]
        
    for section in config.sections(): #old method
        if (
            section.startswith("Profile")
            and config.get(section=section, option="Default", fallback="0")
        ):
            return firefox_dir / config[section]["Path"]
            

    raise RuntimeError("Firefox profile not found")
