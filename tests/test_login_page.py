from pages.login_page import LoginPage
import allure
from time import sleep

username = 'justlavtest@gmail.com'
password = 'testHASLO1#'
incorrect_username = 'bad_test_account@gmail.com'
incorrect_password = 'bad_test_pass'
create_acc_title = 'Создание аккаунта Evernote'


@allure.feature('Login Page')
@allure.story('trying simple login by steps')
def test_normal_login(driver):
    with allure.step('Open page'):
        login_form = LoginPage(driver)
        login_form.open()
    with allure.step('filling username field'):
        login_form.username_field().send_keys(username)
    with allure.step('username conformation'):
        login_form.login_button().submit()
    with allure.step('filling password field'):
        login_form.pass_field().send_keys(password)
    with allure.step('username conformation'):
        login_form.login_button().submit()
    with allure.step('success'):
        assert login_form.login_success() is True


@allure.feature('Login Page')
@allure.story('trying simple login')
def test_login_check(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.simple_login(username, password)


@allure.feature('Login Page')
@allure.story('trying login with checkbox')
def test_login_with_check_box(driver):
    with allure.step('Open page'):
        login_form = LoginPage(driver)
        login_form.open()
    with allure.step('filling username field'):
        login_form.username_field().send_keys(username)
    with allure.step('username conformation'):
        login_form.login_button().submit()
    with allure.step('filling password field'):
        login_form.pass_field().send_keys(password)
    with allure.step('try use checkbox'):
        login_form.check_box().click()
        login_form.check_box().is_selected()
    with allure.step('username conformation'):
        login_form.login_button().submit()
    with allure.step('success'):
        assert login_form.login_success() is True


@allure.feature('Login Page')
@allure.story('trying incorrect login')
def test_bad_login(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(incorrect_username)
    login_form.login_button().submit()
    login_form.login_error()


@allure.feature('Login Page')
@allure.story('trying incorrect  pass')
def test_bad_password(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(username)
    login_form.login_button().submit()
    login_form.pass_field().send_keys(password)
    login_form.login_button().submit()


@allure.feature('Login Page')
@allure.story('check button for creating new acc')
def test_new_account_title(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.create_acc().click()
    assert login_form.page_title_check() == create_acc_title
