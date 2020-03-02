from src.Pages.contactUsPage import ContactUsPageLocators, ContactUsPageHelper
from src.Pages.loginPage import LoginPageHelper


# Authorized user
def test_send_message(browser):
    sign_in_page = LoginPageHelper(browser)
    sign_in_page.go_to_page(ContactUsPageHelper.page_url)
    sign_in_page.enter_credentials()
    sign_in_page.click_sign_in()
    contact_page = ContactUsPageHelper(browser)
    contact_page.go_to_page(ContactUsPageHelper.page_url)
    contact_page.select_subject_heading(1)
    contact_page.select_order(1)
    contact_page.fill_message("Hi! This is test message")
    contact_page.send_message()
    assert "Your message has been successfully sent to our team." in contact_page.element_text\
        (ContactUsPageLocators.locator_alert_box)


def test_send_message_unauthorized_user(browser):
    contact_page = ContactUsPageHelper(browser)
    contact_page.go_to_page(ContactUsPageHelper.page_url)
    contact_page.select_subject_heading(1)
    contact_page.fill_email("test@test.com")
    contact_page.fill_message("Hi! This is test message")
    contact_page.send_message()
    assert "Your message has been successfully sent to our team." in contact_page.element_text\
        (ContactUsPageLocators.locator_alert_box)


def test_send_message_without_subject(browser):
    contact_page = ContactUsPageHelper(browser)
    contact_page.go_to_page(ContactUsPageHelper.page_url)
    contact_page.fill_email("test@test.com")
    contact_page.fill_message("Hi! This is test message")
    contact_page.send_message()
    assert "Please select a subject from the list provided." in contact_page.element_text\
        (ContactUsPageLocators.locator_alert_box)


def test_send_message_without_email(browser):
    contact_page = ContactUsPageHelper(browser)
    contact_page.go_to_page(ContactUsPageHelper.page_url)
    contact_page.select_subject_heading(1)
    contact_page.fill_message("Hi! This is test message")
    contact_page.send_message()
    assert "Invalid email address." in contact_page.element_text\
        (ContactUsPageLocators.locator_alert_box)


def test_send_message_without_body(browser):
    contact_page = ContactUsPageHelper(browser)
    contact_page.go_to_page(ContactUsPageHelper.page_url)
    contact_page.select_subject_heading(1)
    contact_page.fill_email("test@test.com")
    contact_page.send_message()
    assert "The message cannot be blank." in contact_page.element_text\
        (ContactUsPageLocators.locator_alert_box)
