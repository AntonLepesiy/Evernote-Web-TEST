import pytest
from pages.home_page import HomePage
from datetime import datetime


current_datetime = str(datetime.now())
note_title = ' '.join(['Test note: ', current_datetime])
note_body = current_datetime


def test_find_create_new_button(driver_with_cookies, is_logged):
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.create_new_button()


def test_create_new_note(driver_with_cookies, is_logged):
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.create_note(note_title, note_body)
    # home_page.go_home().click()


def test_settings_button_is_displayed(driver_with_cookies, is_logged):  # ok
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.take_first_note()
    home_page.setting_button_is_displayed()


# def test_nots_create(driver_with_cookies, is_logged):
#     home_page = HomePage(driver_with_cookies)
#     home_page.open()
#     home_page.create_note2(note_title, note_body)

def test_nots_create2(driver_with_cookies, is_logged):
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.create_note2()


@pytest.mark.dev
def test_del_second(driver_with_cookies, is_logged):
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.take_second_note()
    home_page.go_to_more_actions_menu()
    home_page.move_to_trash()


@pytest.mark.dev
def test_del_first(driver_with_cookies, is_logged):
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.take_first_note()
    home_page.go_to_more_actions_menu()
    home_page.move_to_trash()


