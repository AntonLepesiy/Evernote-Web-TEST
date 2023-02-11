from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os.path import join, dirname
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage


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
        username = 'justlavtest@gmail.com'
        password = 'testHASLO1#'
        login_check.simple_login(username, password)


@pytest.fixture(scope='function')    # Выдаліць?????????
def driver_and_login():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    driver.get('https://www.evernote.com/Login.action')
    login = driver.find_element(By.ID, 'username')
    log_button = driver.find_element(By.ID, 'loginButton')
    login.send_keys('justlavtest@gmail.com')
    log_button.submit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
    passw = driver.find_element(By.ID, 'password')
    passw.send_keys('testHASLO1#')
    log_button.submit()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'qa-HOME_TITLE')))
    yield chrome_driver
    chrome_driver.quit()
