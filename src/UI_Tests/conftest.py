import pytest
from selenium import webdriver
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#     driver.maximize_window()
#     yield driver
#     driver.quit()


capabilities = {
    "browserName": "chrome",
    "version": "77.0",
    "enableVNC": True,
    "enableVideo": False
}


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(
        command_executor="http://10.20.12.202:4444/wd/hub",
        desired_capabilities=capabilities)
    driver.maximize_window()
    yield driver
    driver.delete_all_cookies()
    driver.close()
