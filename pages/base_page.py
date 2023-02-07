from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def page_title_check(self, title):
        current_title = self.driver.title
        return current_title == title
