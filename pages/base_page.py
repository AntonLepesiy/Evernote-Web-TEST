from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import login_page_locators as loc


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.page_url = ''

    def open(self):
        if self.page_url:
            self.driver.get(self.page_url)
        else:
            raise NotImplementedError

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def find_and_submit(self, locator):
        return self.find(locator).submit()

    def send_key(self, keys):
        return self.send_key(keys)

    def element_wait(self, locator, waiting_time):
        return WebDriverWait(self.driver, waiting_time).until(EC.presence_of_element_located(locator))

    def page_title_check(self):
        current_title = self.driver.title
        return current_title

    def simple_login(self, username, password):
        self.find(loc.USERNAME_FIELD).send_keys(username)
        self.find(loc.LOGIN_BUTTON).click()
        self.element_wait(loc.PASSWORD_FIELD, 10)
        self.find(loc.PASSWORD_FIELD).send_keys(password)
        self.find(loc.CHECK_BOX).click()
        self.find(loc.LOGIN_BUTTON).submit()
        self.element_wait(loc.HOMEPAGE_TITLE, 30)

    def wait(self, time):
        self.driver.implicitly_wait(time)

    def switch_to_iframe(self, i_frame):
        self.driver.switch_to.frame(i_frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def get_page_title(self):
        return self.driver.title
