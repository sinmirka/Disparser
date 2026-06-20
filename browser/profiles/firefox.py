from pathlib import Path
import configparser

def get_firefox_profile() -> Path:
    profiles_ini = (
        Path.home()
        / "AppData"
        / "Roaming"
        / "Mozilla"
        / "Firefox"
        / "profiles.ini"
    )

    config = configparser.ConfigParser()
    config.read(profiles_ini)

    for section in config.sections():
        if config.get(section, "Default", fallback="0") == 1:
            path = Path(config[section]["Path"])
            if config.get(section, "IsRelative", fallback="1") == 1:
                return profiles_ini.parent / path
            
            return path

    raise RuntimeError("Firefox profile not found")