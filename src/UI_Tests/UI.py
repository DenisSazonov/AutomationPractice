import time
from src.UI_Tests.Pages import *
from src.UI_Tests.Pages import MainPageHelper


# Registration
def test_registration(browser):
    new_email = str(time.time()) + "@mail.ru"
    password = str(time.time())
    login_page = LoginPageHelper(browser)
    login_page.go_to_login_page()
    login_page.enter_new_email(new_email)
    login_page.submit_new_email()
    register_page = RegisterNewAccountHelper(browser)
    register_page.create_new_account("Myfirstname", "Mysecondname", password, "Bottle Company", "Bobruisk", "2", "12312", "123123123")
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

################## TO DO ######################

# # Buying
# def test_buying():
#     driver.get("http://automationpractice.com/")
#
#     time.sleep(5)
#     MainPageLocators.proceed_to_checkout_button.click()
#     CheckoutLocators.proceed_button_summary_tab.click()
#     CheckoutLocators.proceed_button_address_tab.click()
#     CheckoutLocators.checkbox_terms.click()
#     CheckoutLocators.proceed_button_shipping_tab.click()
#     CheckoutLocators.cheque_button.click()
#     CheckoutLocators.confirm_order_button.click()
#     assert "Your order on My Store is complete." in driver.page_source
#
#
# # Sign out
# def test_sign_out():
#     MainPageLocators.sign_out_button.click()
#     assert "Sign in" in driver.page_source
