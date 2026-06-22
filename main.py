from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from browser.profiles.firefox import get_firefox_profile
print(str(get_firefox_profile()))

service = Service(log_output="geckodriver.log")

options = webdriver.FirefoxOptions()
options.add_argument("-profile")
options.add_argument(str(get_firefox_profile()))

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://discord.com/app")

input()

driver.quit()