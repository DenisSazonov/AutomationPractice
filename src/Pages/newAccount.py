from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class RegisterNewAccountLocators:
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

    def select_gender(self):
        self.find_element(RegisterNewAccountLocators.locator_gender_radiobutton).click()

    def fill_first_name(self, firstname):
        self.find_element(RegisterNewAccountLocators.locator_firstname).send_keys(firstname)

    def fill_last_name(self, lastname):
        self.find_element(RegisterNewAccountLocators.locator_lastname).send_keys(lastname)

    def fill_password(self, password):
        self.find_element(RegisterNewAccountLocators.locator_registration_password_field).send_keys(password)

    def fill_address(self, address):
        self.find_element(RegisterNewAccountLocators.locator_registration_address).send_keys(address)

    def fill_city(self, city):
        self.find_element(RegisterNewAccountLocators.locator_registration_city).send_keys(city)

    def select_state(self, state):
        self.select_from_dropdown(RegisterNewAccountLocators.locator_state_dropdown, state)

    def fill_postcode(self, postcode):
        self.find_element(RegisterNewAccountLocators.locator_post_code).send_keys(postcode)

    def fill_mobile_phone(self, phone_num):
        self.find_element(RegisterNewAccountLocators.locator_mobile_phone).send_keys(phone_num)

    def click_register(self):
        self.find_element(RegisterNewAccountLocators.locator_register_button).click()
