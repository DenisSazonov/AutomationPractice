from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from configparser import ConfigParser
import os


class AutomationPractice:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=50):
        return WebDriverWait(self.driver, time). \
            until(EC.presence_of_element_located(locator))

    # def find_elements(self, locator, time=10):
    #     return WebDriverWait(self.driver, time). \
    #         until(EC.presence_of_all_elements_located(locator),
    #               message=f"Can't find elements by locator {locator}")

    def go_to_page(self, url):
        return self.driver.get(url)

    def go_to_login_page(self):
        return self.driver.get(self.login_page_url)

    def mouse_over(self, to_element):
        hover = ActionChains(self.driver)
        element = self.find_element(to_element)
        hover.move_to_element(element)
        hover.perform()

    def select_from_dropdown(self, locator, index):
        Select(self.find_element(locator)).select_by_index(index)

    def get_current_url(self):
        return self.driver.current_url

    def element_text(self, locator):
        return self.find_element(locator).text

    def click(self, locator):
        self.find_element(locator).click()

    @staticmethod
    def return_password():
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'credentials.txt')
        config = ConfigParser()
        config.read(file_path)
        password = config.get("credentials", "password")
        return password

    @staticmethod
    def return_email():
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'credentials.txt')
        config = ConfigParser()
        config.read(file_path)
        email = config.get("credentials", "email")
        return email
