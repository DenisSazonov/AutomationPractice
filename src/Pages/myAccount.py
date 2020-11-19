from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class MyAccountLocators:
    locator_my_account = (By.CLASS_NAME, "page-heading")
    locator_sign_out = (By.CLASS_NAME, "logout")


class MyAccountHelper(AutomationPractice):
    def check_my_account(self):
        my_account = self.find_element(MyAccountLocators.locator_my_account)
        return my_account.text
