from selenium.webdriver.common.by import By

HOMEPAGE_TITLE = (By.ID, 'qa-HOME_TITLE')
NEW_BUTTON = (By.ID, 'qa-CREATE_NOTE')
NEW_NOTE = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/span/div/ul[1]/li[1]/button')
NOTE_TITLE = (By.CLASS_NAME, 'AZVFJ s9EjL')
NOTE_BODY = (By.XPATH, '//div[@class="para"]')
NOTES_BUTTON = (By.ID, 'qa-NAV_ALL_NOTES')
NOTES_LIST = (By.CLASS_NAME, 'rv-sticky-node-list')
FIRST_NOTE_IN_LIST = (By.XPATH, '//button[@tabindex="0"]')
SECOND_NOTE_IN_LIST = (By.XPATH, '//button[@tabindex="1"]')
HOME_BUTTON = (By.ID, 'qa-NAV_HOME')
MORE_ACTIONS_MENU = (By.XPATH, '//div[@data-tooltipmark="noteactionsdropdown"]')
MORE_ACTIONS_LIST = (By.XPATH, '//ul[@aria-label="Dropdown List"]')
TRASH_BUTTON = (By.CLASS_NAME, '_832s3r8kdOE_SjKO2aq hANwk8g_6_PVeUc1LRQt '
                               'E_lbv7gA85FrFeRroPBY H_L_ZSC9suMHSq9WGzea epNx6nHXkrOz34MJGnzC')
MOVE_TO_TRASH = (By.LINK_TEXT, 'Move to Trash')
MOVED_TO_TRASH_NOTIFICATION = (By.XPATH, '//div[@class="notification notification-success notification-visible"]')
ACC_NAME = (By.CLASS_NAME, 'mjp8WyYQODySClV2byHt')
