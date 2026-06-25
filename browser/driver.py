from selenium import webdriver
from selenium.webdriver.firefox.service import Service

def create_driver():
    service = Service(log_output="geckodriver.log")
    options = webdriver.FirefoxOptions()

    return webdriver.Firefox(
        options=options,
        service=service
    )