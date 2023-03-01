from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from os.path import join, dirname
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
import secured_test_data as TD


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_with_cookies():
    cookies_directory = join(dirname(__file__), 'cookies')
    options = Options()
    options.add_argument(f'user-data-dir={cookies_directory}')
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def is_logged(driver_with_cookies):
    login_check = HomePage(driver_with_cookies)
    login_check.open()
    if login_check.is_login_check():
        pass
    else:
        username = TD.username
        password = TD.password
        login_check.simple_login(username, password)
