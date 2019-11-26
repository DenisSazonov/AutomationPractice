from selenium.webdriver.common.by import By
from src.UI_Tests.BaseApp import AutomationPractice
from selenium.webdriver.support.ui import Select


class MainPageLocators:
    locator_sign_in_button = (By.CLASS_NAME, "login")
    locator_sign_out_button = (By.CLASS_NAME, "logout")
    locator_product_container = (By.XPATH, "//ul[@id='homefeatured']//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of-tablet-line first-item-of-mobile-line']//div[@class='product-container']")
    locator_proceed_to_checkout_button = (By.XPATH, "//span[contains(text(),'Proceed to checkout')]")
    locator_add_to_cart_button = (By.XPATH, "//li[@class='ajax_block_product col-xs-12 col-sm-4 col-md-3 first-in-line first-item-of-tablet-line first-item-of-mobile-line hovered']//span[contains(text(),'Add to cart')]")


class MainPageHelper(AutomationPractice):
    def click_sign_in(self):
        return self.find_element(MainPageLocators.locator_sign_in_button, time=2).click()

    def add_to_cart(self):
        self.mouse_over(MainPageLocators.locator_product_container)
        self.find_element(MainPageLocators.locator_add_to_cart_button, time=3).click()

    def go_to_checkout(self):
        self.find_element(MainPageLocators.locator_proceed_to_checkout_button).click()

    def logout(self):
        self.find_element(MyAccountLocators.locator_sign_out).click()

    def check_logout(self):
        return self.find_element(MainPageLocators.locator_sign_in_button).text


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
    locator_sign_out = (By.CLASS_NAME, "logout")


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

    def create_new_account(self, firstname, lastname, password, address, city, postcode, phone_num):
        self.find_element(RegisterNewAccoutLocators.locator_gender_radiobutton).click()
        self.find_element(RegisterNewAccoutLocators.locator_firstname).send_keys(firstname)
        self.find_element(RegisterNewAccoutLocators.locator_lastname).send_keys(lastname)
        self.find_element(RegisterNewAccoutLocators.locator_registration_password_field).send_keys(password)
        self.find_element(RegisterNewAccoutLocators.locator_registration_address).send_keys(address)
        self.find_element(RegisterNewAccoutLocators.locator_registration_city).send_keys(city)
        self.select_from_dropdown(RegisterNewAccoutLocators.locator_state_dropdown, 2)
        self.find_element(RegisterNewAccoutLocators.locator_post_code).send_keys(postcode)
        self.find_element(RegisterNewAccoutLocators.locator_mobile_phone).send_keys(phone_num)
        self.find_element(RegisterNewAccoutLocators.locator_register_button).click()


class CheckoutLocators:
    locator_proceed_button_summary_tab = (By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]")
    locator_proceed_button_address_tab = (By.XPATH, "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]")
    locator_proceed_button_shipping_tab = (By.XPATH, "//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]")
    locator_checkbox_terms = (By.XPATH, "//input[@id='cgv']")
    locator_bank_wire_button = (By.XPATH, "//a[@class='bankwire']")
    locator_confirm_order_button = (By.XPATH, "//span[contains(text(),'I confirm my order')]")
    locator_completed_order = (By.CLASS_NAME, "cheque-indent")


class CheckoutLocatorsHelper(AutomationPractice):
    def completion_order(self):
        self.find_element(CheckoutLocators.locator_proceed_button_summary_tab).click()
        self.find_element(CheckoutLocators.locator_proceed_button_address_tab).click()
        self.find_element(CheckoutLocators.locator_checkbox_terms).click()
        self.find_element(CheckoutLocators.locator_proceed_button_shipping_tab).click()
        self.find_element(CheckoutLocators.locator_bank_wire_button).click()
        self.find_element(CheckoutLocators.locator_confirm_order_button).click()

    def check_completed_order(self):
        return self.find_element(CheckoutLocators.locator_completed_order).text
