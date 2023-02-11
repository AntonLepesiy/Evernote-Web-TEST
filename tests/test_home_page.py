from pages.home_page import HomePage


# def test_create_new(driver_with_cookies, is_logged):
#     new_note = HomePage(driver_with_cookies)
#     new_note.open()
#     new_note.create_new_button().click()
#     new_note.note_title().send_keys('test note')
#     new_note.home().click()


def test_settings_button_is_displ(driver_with_cookies, is_logged):  # ok
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.setting_button_is_displayed()


def test_settings_button_is_displ3(driver_with_cookies, is_logged):  # ok
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.setting_button_is_displayed()


def test_settings_button_is_displ2(driver_with_cookies, is_logged):  # ok
    home_page = HomePage(driver_with_cookies)
    home_page.open()
    home_page.setting_button_is_displayed()
