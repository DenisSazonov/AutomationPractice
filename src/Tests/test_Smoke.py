import time
import pytest
from src.Pages.mainPage import MainPageHelper
from src.Pages.loginPage import LoginPageHelper
from src.Pages.checkout import CheckoutHelper
from src.Pages.myAccount import MyAccountHelper, MyAccountLocators
from src.Pages.newAccount import RegisterNewAccountHelper, RegisterNewAccountLocators

# Registration
@pytest.mark.smoke
def test_registration(browser):
    new_email = str(time.time()) + "@mail.ru"
    password = str(time.time())
    login_page = LoginPageHelper(browser)
    login_page.go_to_page(LoginPageHelper.page_url)
    login_page.enter_new_email(new_email)
    login_page.submit_new_email()
    register_page = RegisterNewAccountHelper(browser)
    register_page.fill_first_name("John")
    register_page.fill_last_name("Stalin")
    register_page.fill_password(password)
    register_page.fill_address("My Company")
    register_page.fill_city("Bobruisk")
    register_page.select_state(2)
    register_page.fill_postcode("12312")
    register_page.fill_mobile_phone("123123123")
    register_page.click(RegisterNewAccountLocators.locator_register_button)
    my_account_page = MyAccountHelper(browser)
    success_login = my_account_page.check_my_account()
    assert "MY ACCOUNT" in success_login


# Sign in
@pytest.mark.smoke
def test_login(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.click_sign_in()
    login_page = LoginPageHelper(browser)
    login_page.enter_credentials()
    login_page.click_sign_in()
    my_account_page = MyAccountHelper(browser)
    success_login = my_account_page.check_my_account()
    assert "MY ACCOUNT" in success_login


# Buying
@pytest.mark.smoke
def test_buying(browser):
    main_page = MainPageHelper(browser)
    login_page = LoginPageHelper(browser)
    login_page.go_to_page(LoginPageHelper.page_url)
    login_page.enter_credentials()
    login_page.click_sign_in()
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.add_to_cart()
    time.sleep(3)
    main_page.go_to_checkout()
    checkout = CheckoutHelper(browser)
    checkout.completion_order()
    assert "Your order on My Store is complete." in checkout.check_completed_order()


# Sign out
@pytest.mark.smoke
def test_sign_out(browser):
    main_page = MainPageHelper(browser)
    login_page = LoginPageHelper(browser)
    login_page.go_to_page(LoginPageHelper.page_url)
    login_page.enter_credentials()
    login_page.click_sign_in()
    main_page.click(MyAccountLocators.locator_sign_out)
    assert "Sign in" in main_page.check_logout()
