from selenium.webdriver.common.by import By

USERNAME_FIELD = (By.ID, 'username')
LOGIN_BUTTON = (By.ID, 'loginButton')
PASSWORD_FIELD = (By.ID, 'password')
HOMEPAGE_TITLE = (By.ID, 'qa-HOME_TITLE')
LOGIN_ERROR = (By.XPATH, '//*[@id="responseMessage"]')
CHECK_BOX = (By.XPATH, '//input[@id="rememberMe"]')
CREATE_ACC_LINK = (By.ID, 'switch-link')

