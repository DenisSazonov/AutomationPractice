from src.Pages.loginPage import LoginPageHelper, LoginPageLocators
import pytest



@pytest.mark.parametrize('email', ["!@#$%^&*()", "123", "asd", "   ", ""])
def test_create_account_with_invalid_credentials(browser, email):
    login_page = LoginPageHelper(browser)
    login_page.go_to_page(LoginPageHelper.page_url)
    login_page.enter_new_email(email)
    login_page.click(LoginPageLocators.locator_create_account_button)
    assert "Invalid email address" in login_page.element_text(LoginPageLocators.locator_alert_box_create_account)


@pytest.mark.parametrize('email, password', [("", ""), ("", "1234")])
def test_login_with_invalid_credentials(browser, email, password):
    pass



