from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator = 'div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def field_username(self):
        try:
            self.find_element(locator = 'input[id="user-name"]')
        except NoSuchElementException:
            return False
        return True

    def field_password(self):
        try:
            self.find_element(locator = 'input[id="password"]')
        except NoSuchElementException:
            return False
        return True