from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class MainPageLocators:
    locator_sign_in_button = (By.CSS_SELECTOR, ".login")
    locator_sign_out_button = (By.CLASS_NAME, "logout")
    locator_product_container = (By.CSS_SELECTOR, "#homefeatured>li:nth-child(1)")
    locator_proceed_to_checkout_button = (By.CSS_SELECTOR, ".btn.btn-default.button.button-medium")
    locator_add_to_cart_button = (By.CSS_SELECTOR, "#homefeatured>li:nth-child(1) [data-id-product='1']")
    locator_women_tab = (By.CSS_SELECTOR, ".sf-menu>li>[title='Women']")
    locator_dresses_tab = (By.CSS_SELECTOR, ".sf-menu>li>[title='Dresses']")
    locator_tshirt_tab = (By.CSS_SELECTOR, ".sf-menu>li>[title='T-shirts']")
    locator_newsletter = (By.CSS_SELECTOR, ".alert-danger")
    locator_email_field = (By.CSS_SELECTOR, ".inputNew")
    locator_submit_newsletter = (By.CSS_SELECTOR, "[name='submitNewsletter']")
    locator_alert = (By.CSS_SELECTOR, ".alert")
    locator_facebook = (By.CSS_SELECTOR, ".facebook")
    locator_twitter = (By.CSS_SELECTOR, ".twitter")
    locator_youtube = (By.CSS_SELECTOR, ".youtube")
    locator_gogleplus = (By.CSS_SELECTOR, ".google-plus")


class MainPageHelper(AutomationPractice):

    page_url = "http://automationpractice.com/"

    def click_sign_in(self):
        return self.find_element(MainPageLocators.locator_sign_in_button, time=2).click()

    def add_to_cart(self):
        self.mouse_over(MainPageLocators.locator_product_container)
        self.find_element(MainPageLocators.locator_add_to_cart_button, time=3).click()

    def go_to_checkout(self):
        self.find_element(MainPageLocators.locator_proceed_to_checkout_button).click()

    def check_logout(self):
        return self.find_element(MainPageLocators.locator_sign_in_button).text

    def go_to_top_menu_links(self, tab):
        if tab == "women":
            self.find_element(MainPageLocators.locator_women_tab).click()
        elif tab == "dresses":
            self.find_element(MainPageLocators.locator_dresses_tab).click()
        elif tab == "T-shirt":
            self.find_element(MainPageLocators.locator_tshirt_tab).click()

    def subscribe(self, email):
        self.find_element(MainPageLocators.locator_email_field).send_keys(email)
        self.find_element(MainPageLocators.locator_submit_newsletter).click()

    def go_to_follow_us_links(self, link):
        self.find_element(MainPageLocators.locator_facebook).click()
