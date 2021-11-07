from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # login_form
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#login_form #id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login_form #id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form button[name='login_submit']")
    LOGIN_RESET_PASSWORD_LINK = (By.CSS_SELECTOR, "##login_form a")

    # register_form
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_GALLERY = (By.CSS_SELECTOR, "#product_gallery")
    PRODUCT_MAIN = (By.CSS_SELECTOR, ".product_main")
    PRODUCT_ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, f".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, f".product_main>p.price_color")

    # after product added to basket
    MESSAGES = (By.CSS_SELECTOR, "#messages")
    MESSAGES_ABOUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div.alert-success div.alertinner strong")
    MESSAGES_ABOUT_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div.alert-info div.alertinner p strong")
