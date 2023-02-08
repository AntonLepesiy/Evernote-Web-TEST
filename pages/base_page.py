from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
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

    def standard_login(self):
        self.driver.get('https://www.evernote.com/Login.action')
        self.driver.find_element(By.ID, 'username').send_keys('justlavtest@gmail.com')
        self.driver.find_element(By.ID, 'loginButton').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.driver.find_element(By.ID, 'password')))
        self.driver.find_element(By.ID, 'password').send_keys('testHASLO1#')
        self.driver.find_element(By.ID, 'loginButton').submit()
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.driver.find_element(By.ID, 'qa-HOME_TITLE')))
