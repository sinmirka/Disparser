from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx

def get_default_browser():
    key_path = (
        r"Software\Microsoft\Windows\Shell\Associations"
        r"\UrlAssociations\http\UserChoice"
    )