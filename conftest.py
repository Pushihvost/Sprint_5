import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.urls import BASE_URL

@pytest.fixture
def driver():
    service = Service("C:\\WebDriver\\bin\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()
