import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

product_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'


class TestUserAddToBasketFromProductPage:

    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        pass

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_product_page()

        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        page.should_be_success_messages()
        page.basket_price_should_be_equal_product_price()
        page.message_product_name_should_be_equal_actual_product_name()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_product_page()

        assert page.is_not_element_present(
            ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME), "Success message is present"


@pytest.mark.skip
@pytest.mark.parametrize(
    'promo_link',
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                  marks=pytest.mark.xfail),
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
)
def test_guest_can_add_product_to_basket(promo_link, browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_messages()
    page.basket_price_should_be_equal_product_price()
    page.message_product_name_should_be_equal_actual_product_name()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    assert page.is_not_element_present(ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME), "Success message is present"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()

    assert page.is_not_element_present(ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME), "Success message is present"


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    assert page.is_disappeared(ProductPageLocators.MESSAGES_ABOUT_PRODUCT_NAME), "Success message is still present"
