from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class CheckoutLocators:
    locator_proceed_button_summary_tab = (By.CSS_SELECTOR, "p>a[title='Proceed to checkout']")
    locator_proceed_button_address_tab = (By.CSS_SELECTOR, "p>button[name='processAddress']")
    locator_proceed_button_shipping_tab = (By.CSS_SELECTOR, "p>button[name='processCarrier']")
    locator_checkbox_terms = (By.ID, "cgv")
    locator_bank_wire_button = (By.CSS_SELECTOR, "[class='bankwire']")
    locator_confirm_order_button = (By.CSS_SELECTOR, "p [type='submit']")
    locator_completed_order = (By.CLASS_NAME, "cheque-indent")


class CheckoutHelper(AutomationPractice):
    def completion_order(self):
        self.find_element(CheckoutLocators.locator_proceed_button_summary_tab).click()
        self.find_element(CheckoutLocators.locator_proceed_button_address_tab).click()
        self.find_element(CheckoutLocators.locator_checkbox_terms).click()
        self.find_element(CheckoutLocators.locator_proceed_button_shipping_tab).click()
        self.find_element(CheckoutLocators.locator_bank_wire_button).click()
        self.find_element(CheckoutLocators.locator_confirm_order_button).click()

    def check_completed_order(self):
        return self.find_element(CheckoutLocators.locator_completed_order).text