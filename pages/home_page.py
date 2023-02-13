from selenium.common import TimeoutException
from pages.base_page import BasePage
from pages.locators import home_page_locators as loc
import allure


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = 'https://' \
                        'www.evernote.com/client/web?_sourcePage=9cIcmiAKbLHiMUD9T65RG_YvRLZ-1eYO3fqfqRu0fynRL_' \
                        '1nukNa4gH1t86pc1SP&__fp=G5A4Wy5tnWI3yWPvuidLz-TPR6I9Jhx8&hpts=1675875507447&showSwitch' \
                        'Service=true&usernameImmutable=false&login=&login=%D0%92%D0%BE%D0%B9%D1%82%D0%B8&login' \
                        '=true&hptsh=mvstlk5ADUf%2BghX07ak2TurPSgk%3D#?hm=true&'

    def login_success(self):
        self.element_wait(loc.HOMEPAGE_TITLE, 5)

    def get_acc_name(self):
        self.element_wait(loc.USER_PORTRAIT, 10)
        self.find(loc.USER_PORTRAIT).click()
        self.element_wait(loc.USER_MAIL, 150)
        displayed_name = self.find(loc.USER_MAIL).text
        return displayed_name

    def check_page(self, page_title):
        opened_page = self.get_page_title()
        return opened_page == page_title

    def create_new_button(self):
        return self.find(loc.NEW_BUTTON)

    def create_new_note(self):
        self.find(loc.NEW_NOTE_BUTTON_IN_LEFT)

    def note_title(self):
        self.find(loc.NOTE_TITLE)

    def go_home(self):
        self.find(loc.HOME_BUTTON).click()

    def is_login_check(self):
        try:
            self.element_wait(loc.HOMEPAGE_TITLE, 3)
        except TimeoutException:
            return False
        return True

    def setting_button_is_displayed(self):
        return self.find(loc.MORE_ACTIONS_MENU).is_displayed()

    def create_note_with_button_in_left_menu(self, note_title, body_text):
        current_note_title = ''.join(['left', note_title])
        self.find(loc.NEW_BUTTON).click()
        self.find(loc.NEW_NOTE_BUTTON_IN_LEFT).click()
        i_frame = self.find(loc.IFRAME)
        self.switch_to_iframe(i_frame)
        self.element_wait(loc.NOTE_TITLE, 10)
        self.find(loc.NOTE_TITLE).send_keys(current_note_title)
        self.find(loc.NOTE_BODY).send_keys(body_text)
        self.switch_to_default()
        self.find(loc.HOME_BUTTON).click()
        self.find(loc.NOTES_BUTTON_IN_LEFT_MENU).click()
        self.find(loc.FIRST_NOTE_IN_LIST).click()
        i_frame = self.find(loc.IFRAME)
        self.switch_to_iframe(i_frame)
        self.element_wait(loc.NOTE_TITLE, 10)
        return self.find(loc.NOTE_TITLE).is_displayed()

    def create_note_with_button_in_homepage_body(self, note_title, body_text):
        current_note_title = ''.join(['body', note_title])
        self.element_wait(loc.NOTES_BUTTON_IN_BODY, 10)
        self.find(loc.NOTES_BUTTON_IN_BODY).click()
        i_frame = self.find(loc.IFRAME)
        self.switch_to_iframe(i_frame)
        self.element_wait(loc.NOTE_TITLE, 10)
        self.find(loc.NOTE_TITLE).send_keys(current_note_title)
        self.find(loc.NOTE_BODY).send_keys(body_text)
        self.switch_to_default()
        self.find(loc.HOME_BUTTON).click()
        self.find(loc.NOTES_BUTTON_IN_LEFT_MENU).click()
        self.find(loc.FIRST_NOTE_IN_LIST).click()
        i_frame = self.find(loc.IFRAME)
        self.switch_to_iframe(i_frame)
        self.element_wait(loc.NOTE_TITLE, 10)
        return self.find(loc.NOTE_TITLE).is_displayed()

    def take_first_note(self):
        with allure.step('go to the notes list'):
            self.element_wait(loc.NOTES_BUTTON_IN_LEFT_MENU, 15)
            self.find(loc.NOTES_BUTTON_IN_LEFT_MENU).click()
        with allure.step('take first note is notes list'):
            self.find(loc.FIRST_NOTE_IN_LIST).click()

    def take_second_note(self):
        self.element_wait(loc.NOTES_BUTTON_IN_LEFT_MENU, 15)
        self.find(loc.NOTES_BUTTON_IN_LEFT_MENU).click()
        self.find(loc.FIRST_NOTE_IN_LIST).click()

    def go_to_more_actions_menu(self):
        self.find(loc.MORE_ACTIONS_MENU).click()
        self.element_wait(loc.MORE_ACTIONS_LIST, 5)

    def move_to_trash(self):  # click "move to trash in more_actions_list"
        self.find(loc.MOVE_TO_TRASH).click()
        self.element_wait(loc.MOVED_TO_TRASH_NOTIFICATION, 10)

