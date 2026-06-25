from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(log_output="geckodriver.log")

options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(service=service, options=options)
driver.get("https://discord.com/app")

input()

driver.quit()