from pages.home_page import HomePage


def test_create_new(driver_with_cookies, is_logged):
    new_note = HomePage(driver_with_cookies)
    new_note.open()
    new_note.create_new_button().click()
    new_note.note_title().send_keys('test note')
    new_note.home().click()


