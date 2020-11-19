from selenium.webdriver.common.by import By
from src.BaseApp import AutomationPractice


class ProductPageLocators:
    locator_content_scene_cat = (By.CSS_SELECTOR, ".content_scene_cat")


class ProductPageHelper(AutomationPractice):
    def get_txt(self):
        return self.element_text(ProductPageLocators.locator_content_scene_cat)
