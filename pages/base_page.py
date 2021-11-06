from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def is_element_present(self, search_method, search_string):
        try:
            self.browser.find_element(search_method, search_string)
        except NoSuchElementException:
            return False
        return True
