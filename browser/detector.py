from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

def get_default_browser() -> str:
    key_path = (
        r"Software\Microsoft\Windows\Shell\Associations"
        r"\UrlAssociations\http\UserChoice"
    )

    with OpenKey(HKEY_CURRENT_USER, key_path) as key:
        prog_id, _ = QueryValueEx(key, "ProgId")

    return prog_id