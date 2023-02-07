from pages.login_page import LoginPage


username = 'justlavtest@gmail.com'
incorrect_username = 'bad_test_account@gmail.com'
password = 'testHASLO1#'
incorrect_password = 'bad_test_pass'
create_acc_title = 'Создание аккаунта Evernote'


def test_normal_login(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(username)
    login_form.login_button().submit()
    login_form.pass_field().send_keys(password)
    login_form.login_button().submit()
    login_form.login_success()


def test_login_check(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.standard_login(username, password)


def test_login_with_check_box(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(username)
    login_form.login_button().submit()
    login_form.pass_field().send_keys(password)
    login_form.check_box().click()
    login_form.check_box().is_selected()
    login_form.login_button().submit()
    login_form.login_success()


def test_bad_login(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(incorrect_username)
    login_form.login_button().submit()
    login_form.login_error().is_displayed()


def test_bad_password(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.username_field().send_keys(username)
    login_form.login_button().submit()
    login_form.pass_field().send_keys(password)
    login_form.login_button().submit()


def test_new_account_title(driver):
    login_form = LoginPage(driver)
    login_form.open()
    login_form.create_acc().click()
    login_form.page_title_check(create_acc_title)
