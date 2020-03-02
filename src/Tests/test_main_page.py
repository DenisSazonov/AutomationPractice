from src.Pages.productPages import ProductPageHelper
from src.Pages.mainPage import MainPageHelper, MainPageLocators
from src.BaseApp import AutomationPractice
import time


def test_navigating_general_tab_women(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.go_to_top_menu_links("women")
    dresses_page = ProductPageHelper(browser)
    banner = dresses_page.get_txt()
    assert "Women" in banner


def test_navigating_general_tab_dresses(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.go_to_top_menu_links("dresses")
    dresses_page = ProductPageHelper(browser)
    banner = dresses_page.get_txt()
    assert "Dresses" in banner


def test_navigating_general_tab_tshirt(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.go_to_top_menu_links("T-shirt")
    dresses_page = ProductPageHelper(browser)
    banner = dresses_page.get_txt()
    assert "T-shirt" in banner


def test_footer_newsletter_positive(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.subscribe(str(time.time()) + "@mail.ru")
    success = main_page.element_text(MainPageLocators.locator_alert)
    assert "Newsletter : You have successfully subscribed to this newsletter." in success


def test_footer_newsletter_negative(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.subscribe("mail.ru")
    success = main_page.element_text(MainPageLocators.locator_alert)
    assert "Newsletter : Invalid email address." in success


def test_follow_us_links(browser):
    main_page = MainPageHelper(browser)
    main_page.go_to_page(MainPageHelper.page_url)
    main_page.click(MainPageLocators.locator_facebook)
    main_page.driver.switch_to.window(main_page.driver.window_handles[-1])
    url = main_page.get_current_url()
    assert "https://www.facebook.com/groups/525066904174158/" == url
    main_page.driver.close()
    main_page.driver.switch_to.window(main_page.driver.window_handles[0])
    main_page.click(MainPageLocators.locator_twitter)
    main_page.driver.switch_to.window(main_page.driver.window_handles[-1])
    url = main_page.get_current_url()
    assert 'https://twitter.com/seleniumfrmwrk' == url
    main_page.driver.close()
    main_page.driver.switch_to.window(main_page.driver.window_handles[0])
    main_page.click(MainPageLocators.locator_youtube)
    main_page.driver.switch_to.window(main_page.driver.window_handles[-1])
    url = main_page.get_current_url()
    assert 'https://www.youtube.com/channel/UCHl59sI3SRjQ-qPcTrgt0tA' == url
    main_page.driver.close()
    main_page.driver.switch_to.window(main_page.driver.window_handles[0])
    main_page.click(MainPageLocators.locator_gogleplus)
    main_page.driver.switch_to.window(main_page.driver.window_handles[-1])
    url = main_page.get_current_url()
    assert 'accounts.google.com' in url
