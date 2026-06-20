from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service(log_output="geckodriver.log")

driver = webdriver.Firefox(service=service)
driver.get("https://discord.com/app")

input()

driver.quit()