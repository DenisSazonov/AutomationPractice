import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()


# capabilities = {
#     "browserName": "chrome",
#     "version": "78.0",
#     "enableVNC": True,
#     "enableVideo": False
# }
#
#
# @pytest.fixture(scope="function")
# def browser():
#     driver = webdriver.Remote(
#         command_executor="http://10.20.12.202:4444/wd/hub",
#         desired_capabilities=capabilities)
#     driver.maximize_window()
#     yield driver
#     driver.delete_all_cookies()
#     driver.quit()


# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default='ru', help="Choose language")