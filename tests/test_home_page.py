import pytest
from pages.home_page import HomePage
from datetime import datetime
import allure
import secured_test_data as TD

current_datetime = str(datetime.now())
note_title = ' '.join(['Test note: ', current_datetime])
note_body = current_datetime
acc_name = TD.username
page_title = 'Home - Evernote'


@pytest.mark.smoke
@allure.feature('HomePage')
@allure.story('Page is open correctly')
def test_page_is_open(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('Getting page title'):
        home_page.check_page(page_title)


@pytest.mark.simple
@allure.feature('HomePage')
@allure.story('User is logged')
def test_hou_is_logged(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('Check account name'):
        assert home_page.get_acc_name() == acc_name


@pytest.mark.simple
@allure.feature('HomePage')
@allure.story('\"create new\" button is visible in the page')
def test_find_create_new_button(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('searching for \"create new\" button'):
        home_page.create_new_button()


@allure.feature('HomePage')
@allure.story('create new one note with button in the page\'s left side')
def test_create_and_check_new_note_left(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('try to create some note'):
        assert home_page.create_note_with_button_in_left_menu(note_title, note_body)


@allure.feature('HomePage')
@allure.story('create new one note with button in the page\'s body')
def test_create_and_check_new_note_body(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('try to create some note'):
        assert home_page.create_note_with_button_in_homepage_body(note_title, note_body)


@allure.feature('HomePage')
@allure.story('button \"settings\" is available on the page')
def test_settings_button_is_displayed(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('go to first note in the notes list'):
        home_page.take_first_note()
    with allure.step('check visibility of \"settings\" button'):
        assert home_page.setting_button_is_displayed() is True


@allure.feature('HomePage')
@allure.story('try to delete second note in the notes list')
@pytest.mark.smoke
def test_del_second(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('go to second note in the notes list'):
        home_page.take_second_note()
    with allure.step('open menu'):
        home_page.go_to_more_actions_menu()
    with allure.step('remove the note'):
        home_page.move_to_trash()


@allure.feature('HomePage')
@allure.story('try to delete first note in the notes list')
@pytest.mark.smoke
def test_del_first(driver_with_cookies, is_logged):
    with allure.step('Open page'):
        home_page = HomePage(driver_with_cookies)
        home_page.open()
    with allure.step('go to first note in the notes list'):
        home_page.take_first_note()
    with allure.step('open menu'):
        home_page.go_to_more_actions_menu()
    with allure.step('remove the note'):
        home_page.move_to_trash()
