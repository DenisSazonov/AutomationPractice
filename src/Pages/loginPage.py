from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class LoginPageLocators:
    locator_new_email_field = (By.ID, "email_create")
    locator_create_account_button = (By.ID, "SubmitCreate")
    locator_email_field = (By.ID, "email")
    locator_password_field = (By.ID, "passwd")
    locator_login_button = (By.ID, "SubmitLogin")
    locator_alert_box_create_account = (By.CSS_SELECTOR, ".alert ol:nth-child(1)")
    locator_main_alert_box = (By.CSS_SELECTOR, ".alert ol:nth-child(2)")


class LoginPageHelper(AutomationPractice):

    page_url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def enter_credentials(self):
        email_field = self.find_element(LoginPageLocators.locator_email_field)
        email = AutomationPractice.return_email()
        email_field.send_keys(email)
        password_field = self.find_element(LoginPageLocators.locator_password_field)
        password = AutomationPractice.return_password()
        password_field.send_keys(password)
        return password_field, email_field

    def click_sign_in(self):
        return self.find_element(LoginPageLocators.locator_login_button).click()

    def enter_new_email(self, new_email):
        new_email_field = self.find_element(LoginPageLocators.locator_new_email_field)
        new_email_field.send_keys(new_email)
        return new_email_field

    def submit_new_email(self):
        return self.find_element(LoginPageLocators.locator_create_account_button).click()
