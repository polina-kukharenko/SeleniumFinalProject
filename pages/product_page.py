from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = None
    product_price = None

    def should_be_product_page(self):
        self.should_be_product_card()
        self.should_be_add_to_basket_form()
        self.get_product_info()

    def should_be_product_card(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_GALLERY), "Product gallery is not presented"
        assert self.is_element_present(ProductPageLocators.PRODUCT_MAIN), "Product main is not presented"

    def should_be_add_to_basket_form(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_ADD_TO_BASKET_FORM), \
            "Add to basket form is not presented"

    def get_product_info(self):
        self.product_name = self.get_element(ProductPageLocators.PRODUCT_NAME).text
        self.product_price = self.get_element(ProductPageLocators.PRODUCT_PRICE).text
        assert self.product_name, "Product has no name"
        assert self.product_price, "Product has no price"

    def add_product_to_basket(self):
        assert self.is_element_present(ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"
        self.get_element(ProductPageLocators.PRODUCT_ADD_TO_BASKET_BUTTON).click()

    def should_be_success_messages(self):
        assert self.is_element_present(ProductPageLocators.MESSAGES), \
            "Messages element is not presented"

    def should_not_be_success_messages(self):
        assert self.is_not_element_present(ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME), \
            "Success message about product name is presented, but should not be"
        assert self.is_not_element_present(ProductPageLocators.MESSAGES_ABOUT_BASKET_PRICE), \
            "Success message about basket price is presented, but should not be"

    def basket_price_should_be_equal_product_price(self):
        message_basket_price = self.get_element(ProductPageLocators.MESSAGES_ABOUT_BASKET_PRICE)
        assert message_basket_price.text == self.product_price, \
            "Basket price not equal to product price"

    def message_product_name_should_be_equal_actual_product_name(self):
        message_basket_product_name = self.get_element(ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME)
        assert message_basket_product_name.text == self.product_name, \
            "Product name in message not equal to actual product name"
