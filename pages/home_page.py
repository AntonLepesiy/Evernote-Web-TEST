from selenium.common import TimeoutException
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
        return self.element_wait(loc.HOMEPAGE_TITLE, 5)

    def create_new(self):
        self.find(loc.NEW_BUTTON).click()

    def note_title(self):
        return self.find(loc.NOTE_TITLE)

    def home(self):
        return self.find(loc.HOME_BUTTON)

    def is_login_check(self):
        try:
            self.element_wait(loc.HOMEPAGE_TITLE, 3)
        except TimeoutException:
            return False
        return True

    def setting_button_is_displayed(self):
        return self.find(loc.SETTINGS_BUTTON).is_displayed()

    # def get_acc_name(self):
    #     acc_name =  "justlavtest@gmail.com"
    #     displaed_name = self.find(loc.ACC_NAME).
    #     return
