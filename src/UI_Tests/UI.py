import time
from src.UI_Tests.Pages import *


# Registration
def test_registration(browser):
    new_email = str(time.time()) + "@mail.ru"
    password = str(time.time())
    login_page = LoginPageHelper(browser)
    login_page.go_to_login_page()
    login_page.enter_new_email(new_email)
    login_page.submit_new_email()
    register_page = RegisterNewAccountHelper(browser)
    register_page.create_new_account("Myfirstname", "Mysecondname", password, "Bottle Company", "Bobruisk",
                                     "12312", "123123123")
    my_account_page = MyAccountHelper(browser)
    success_login = my_account_page.check_my_account()
    assert "MY ACCOUNT" in success_login
    login_page.teardown()


# Sign in
def test_login(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.click_sign_in()
    login_page = LoginPageHelper(browser)
    login_page.go_to_login_page()
    login_page.enter_credentials("test@test.ru", "123456")
    login_page.click_sign_in()
    my_account_page = MyAccountHelper(browser)
    success_login = my_account_page.check_my_account()
    assert "MY ACCOUNT" in success_login
    login_page.teardown()


# Buying
def test_buying(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.click_sign_in()
    login_page = LoginPageHelper(browser)
    login_page.go_to_login_page()
    login_page.enter_credentials("test@test.ru", "123456")
    login_page.click_sign_in()
    main_page.go_to_site()
    main_page.add_to_cart()
    time.sleep(3)
    main_page.go_to_checkout()
    checkout = CheckoutHelper(browser)
    checkout.completion_order()
    assert "Your order on My Store is complete." in checkout.check_completed_order()
    checkout.teardown()


# Sign out
def test_sign_out(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_site()
    main_page.click_sign_in()
    login_page = LoginPageHelper(browser)
    login_page.go_to_login_page()
    login_page.enter_credentials("test@test.ru", "123456")
    login_page.click_sign_in()
    main_page.logout()
    assert "Sign in" in main_page.check_logout()
    main_page.teardown()
