import re
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return self.extract_price(price_text)

    def extract_price(self, text):
        """Извлекает число с плавающей точкой из строки с ценой"""
        match = re.search(r"\d+\.\d+", text)
        return float(match.group()) if match else None

    def should_be_success_message_with_product_name(self, expected_name):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text
        assert (
            expected_name in success_message
        ), "Название товара не совпадает в сообщении об успехе"

    def should_be_basket_price_equal_to_product_price(self, expected_price):
        basket_price_text = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text
        basket_price = self.extract_price(basket_price_text)
        print(f"Ожидаемая цена: {expected_price}")
        print(f"Цена в корзине: {basket_price}")
        assert (
            expected_price == basket_price
        ), "Цена в корзине не совпадает с ценой товара"
