from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_messages_element()
    page.basket_price_should_be_equal_product_price()
    page.message_product_name_should_be_equal_actual_product_name()
