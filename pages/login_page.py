from pages.base_page import BasePage
from pages.locators import login_page_locators as loc


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://www.evernote.com/Login.action'

    def simple_login(self, username, password):
        self.find(loc.USERNAME_FIELD).send_keys(username)
        self.find(loc.LOGIN_BUTTON).click()
        self.element_wait(loc.PASSWORD_FIELD, 10)
        self.find(loc.PASSWORD_FIELD).send_keys(password)
        self.find(loc.LOGIN_BUTTON).submit()
        self.element_wait(loc.HOMEPAGE_TITLE, 15)

    def username_field(self):
        return self.find(loc.USERNAME_FIELD)

    def login_button(self):
        return self.find(loc.LOGIN_BUTTON)

    def login_error(self):
        self.element_wait(loc.LOGIN_ERROR, 10)
        return self.find(loc.LOGIN_ERROR).is_displayed()

    def pass_field(self):
        self.element_wait(loc.PASSWORD_FIELD, 10)
        return self.find(loc.PASSWORD_FIELD)

    def login_success(self):
        self.element_wait(loc.HOMEPAGE_TITLE, 15)
        return self.find(loc.HOMEPAGE_TITLE).is_displayed()

    def check_box(self):
        return self.find(loc.CHECK_BOX)

    def create_acc(self):
        return self.find(loc.CREATE_ACC_LINK)
