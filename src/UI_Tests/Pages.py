from selenium.webdriver.common.by import By
from src.UI_Tests.BaseApp import AutomationPractice
from selenium.webdriver.support.ui import Select

class MainPageLocators:
    locator_sign_in_button = (By.CLASS_NAME, "login")
    locator_sign_out_button = (By.XPATH, "//a[@class='logout']")
    locator_product_container = (By.CLASS_NAME, "product-container")
    locator_proceed_to_checkout_button = (By.CLASS_NAME, "btn btn-default button button-medium")
    locator_add_to_cart_button = (By.XPATH, "//li//span[contains(text(),'Add to cart')]")


class MainPageHelper(AutomationPractice):
    def click_sign_in(self):
        return self.find_element(MainPageLocators.locator_sign_in_button, time=2).click

    def add_product_to_cart(self):
        self.mouse_over(MainPageLocators.locator_product_container).perform()
        return self.find_element(MainPageLocators.locator_add_to_cart_button).click


class LoginPageLocators:
    locator_new_email_field = (By.XPATH, "//input[@id='email_create']")
    locator_create_account_button = (By.CSS_SELECTOR, "#SubmitCreate")
    locator_email_field = (By.ID, "email")
    locator_password_field = (By.ID, "passwd")
    locator_login_button = (By.ID, "SubmitLogin")


class LoginPageHelper(AutomationPractice):

    def enter_credentials(self, login, password):
        email_field = self.find_element(LoginPageLocators.locator_email_field)
        email_field.send_keys(login)
        password_field = self.find_element(LoginPageLocators.locator_password_field)
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


class MyAccountLocators:
    locator_my_account = (By.CLASS_NAME, "page-heading")


class MyAccountHelper(AutomationPractice):
    def check_my_account(self):
        my_account = self.find_element(MyAccountLocators.locator_my_account)
        return my_account.text

class RegisterNewAccoutLocators:
    locator_gender_radiobutton = (By.ID, "uniform-id_gender1")
    locator_firstname = (By.ID, "customer_firstname")
    locator_lastname = (By.ID, "customer_lastname")
    locator_registration_password_field = (By.ID, "passwd")
    locator_registration_address = (By.ID, "address1")
    locator_registration_city = (By.ID, "city")
    locator_state_dropdown = (By.ID, "id_state")
    locator_post_code = (By.ID, "postcode")
    locator_mobile_phone = (By.ID, "phone_mobile")
    locator_register_button = (By.ID, "submitAccount")


class RegisterNewAccountHelper(AutomationPractice):

    def create_new_account(self, firstname, lastname, password, address, city, state, postcode, phone_num):
        self.find_element(RegisterNewAccoutLocators.locator_gender_radiobutton).click()
        self.find_element(RegisterNewAccoutLocators.locator_firstname).send_keys(firstname)
        self.find_element(RegisterNewAccoutLocators.locator_lastname).send_keys(lastname)
        self.find_element(RegisterNewAccoutLocators.locator_registration_password_field).send_keys(password)
        self.find_element(RegisterNewAccoutLocators.locator_registration_address).send_keys(address)
        self.find_element(RegisterNewAccoutLocators.locator_registration_city).send_keys(city)
        Select(self.find_element(RegisterNewAccoutLocators.locator_state_dropdown)).select_by_index(2)
        # self.select_from_dropdown(RegisterNewAccoutLocators.locator_state_dropdown).select_by_index(state)
        self.find_element(RegisterNewAccoutLocators.locator_post_code).send_keys(postcode)
        self.find_element(RegisterNewAccoutLocators.locator_mobile_phone).send_keys(phone_num)
        self.find_element(RegisterNewAccoutLocators.locator_register_button).click()


class CheckoutLocators:
    locator_proceed_button_summary_tab = (By.CLASS_NAME, "btn btn-default button button-medium")
    locator_proceed_button_address_tab = (By.CLASS_NAME, "button btn btn-default button-medium")
    locator_proceed_button_shipping_tab = (By.CLASS_NAME, "button btn btn-default standard-checkout button-medium")
    locator_checkbox_terms = (By.ID, "uniform-cgv")
    locator_cheque_button = (By.CLASS_NAME, "cheque")
    locator_confirm_order_button = (By.CLASS_NAME, "button btn btn-default button-medium")

