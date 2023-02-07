from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

