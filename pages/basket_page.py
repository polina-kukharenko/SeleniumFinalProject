from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_goods_element()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "Not 'basket' url"

    def should_be_goods_element(self):
        assert self.is_element_present(BasketPageLocators.BASKET_GOODS), "Basket goods element is not present"

    def is_basket_empty(self):
        assert self.get_element(BasketPageLocators.BASKET_EMPTY), "Basket not empty"

