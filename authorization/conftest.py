import pytest
from selenium import webdriver
import pickle
from time import *


@pytest.fixture(scope='function')
def open_browser_selenoid_without_cookies():
    capabilities = {
        'screenResolution': '1080x1280x24',
        "browserName": "chrome",
        "version": "84.0",
        "enableVNC": True,
        "enableVideo": False,
    }
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

