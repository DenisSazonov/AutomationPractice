from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class ContactUsPageLocators:
    locator_subject_heading_dropdown = (By.ID, "id_contact")
    locator_email_field = (By.CSS_SELECTOR, "#email")
    locator_order_reference_dropdown = (By.CSS_SELECTOR, "[name = 'id_order']")
    locator_file_upload_field = (By.CSS_SELECTOR, "input#fileUpload")
    locator_message_field = (By.CSS_SELECTOR, "#message")
    locator_submit_button = (By.CSS_SELECTOR, "#submitMessage")
    locator_alert_box = (By.CSS_SELECTOR, ".alert")


class ContactUsPageHelper(AutomationPractice):

    page_url = "http://automationpractice.com/index.php?controller=contact"

    def select_subject_heading(self, subject):
        self.select_from_dropdown(ContactUsPageLocators.locator_subject_heading_dropdown, subject)

    def fill_email(self, email):
        self.find_element(ContactUsPageLocators.locator_email_field).send_keys(email)

    def select_order(self, order):
        self.select_from_dropdown(ContactUsPageLocators.locator_order_reference_dropdown, order)

    def fill_message(self, message):
        self.find_element(ContactUsPageLocators.locator_message_field).send_keys(message)

    def send_message(self):
        self.find_element(ContactUsPageLocators.locator_submit_button).click()
