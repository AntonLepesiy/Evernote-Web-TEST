from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import home_page_locators as loc


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

    def create_new_button(self):
        return self.find(loc.NEW_BUTTON)

    def create_new_note(self):
        self.find(loc.NEW_NOTE)

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
        self.find(loc.MORE_ACTIONS_MENU).is_displayed()

    def create_note(self, note_title, body_text):
        self.find(loc.NEW_BUTTON).click()
        self.find(loc.NEW_NOTE).click()
        self.element_wait(loc.NOTE_TITLE, 10)
        # # self.find(loc.NOTE_TITLE).send_keys(note_title)
        # self.find(loc.NOTE_BODY).send_keys(body_text)
        # self.find(loc.HOME_BUTTON).click()

    def create_note2(self):
        self.find(loc.NEW_BUTTON).click()
        self.find(loc.NEW_NOTE).click()
        self.wait(10)
        self.element_wait(loc.NOTE_TITLE, 10)

    # def get_acc_name(self):
    #     acc_name =  "justlavtest@gmail.com"
    #     displaed_name = self.find(loc.ACC_NAME).
    #     return

    def take_first_note(self):
        self.element_wait(loc.NOTES_BUTTON, 15)
        self.find(loc.NOTES_BUTTON).click()
        self.find(loc.FIRST_NOTE_IN_LIST).click()

    def take_second_note(self):
        self.element_wait(loc.NOTES_BUTTON, 15)
        self.find(loc.NOTES_BUTTON).click()
        self.find(loc.FIRST_NOTE_IN_LIST).click()

    def go_to_more_actions_menu(self):
        self.find(loc.MORE_ACTIONS_MENU).click()
        self.element_wait(loc.MORE_ACTIONS_LIST, 5)

    def move_to_trash(self):  # click "move to trash in more_actions_list"
        self.find(loc.MOVE_TO_TRASH).click()
        self.element_wait(loc.MOVED_TO_TRASH_NOTIFICATION, 10)
