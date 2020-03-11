import pytest
from selenium import webdriver
import os
from datetime import datetime

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    browser.maximize_window()
    failed_before = request.session.testsfailed
    yield browser
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(browser, test_name)
    browser.quit()

def take_screenshot(browser, test_name):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshots_dir = os.path.abspath(os.path.dirname(__file__)) + "\screenshots_failed_tests"
    screenshot_file_path = "{}/{} {}.png".format(screenshots_dir, now, test_name)
    if not os.path.exists(screenshots_dir):
        os.mkdir(screenshots_dir)
        browser.save_screenshot(screenshot_file_path)
    else:
        browser.save_screenshot(screenshot_file_path)

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
