import pytest
import time

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        user_email = f'{str(time.time())}@fakemail.org'
        user_password = str(time.time())

        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_login_page()
        register_page = LoginPage(browser, browser.current_url)
        register_page.should_be_register_form()

        register_page.register_new_user(user_email, user_password)
        register_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_product_page()
        page.add_product_to_basket()
        page.should_be_success_messages()
        page.basket_price_should_be_equal_product_price()
        page.message_product_name_should_be_equal_actual_product_name()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_product_page()
        page.cant_see_success_message()


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
def test_guest_can_add_product_to_basket_promo(promo_link, browser):
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_messages()
    page.basket_price_should_be_equal_product_price()
    page.message_product_name_should_be_equal_actual_product_name()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()
    page.add_product_to_basket()
    page.should_be_success_messages()
    page.basket_price_should_be_equal_product_price()
    page.message_product_name_should_be_equal_actual_product_name()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    page.cant_see_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()
    page.cant_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    page.success_page_should_be_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.is_basket_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
