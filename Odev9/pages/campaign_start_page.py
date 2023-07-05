import random
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignStartPage(BasePage):
    CAMPAIGN_CREATE_BUTTON = (By.ID, "create-mobile-campaign")
    CAMPAIGN_NAME_INPUT = (By.ID, "campaign-name")
    CAMPAIGN_PLATFORM_TYPE_SELECTION = (By.CLASS_NAME, "qa-segments-web")
    CAMPAIGN_CREATE_CONFIRM = (By.ID, "accept")
    NEXT_BUTTON = (By.ID, "save-and-next")
    test_number = random.randint(0, 1000000)
    SLIDE_MENU_ICON = (By.XPATH, ".//*[contains(@class,'routes')]//*[contains(@class,'groups')][3]")
    MENU_SELECTOR = ".//*[contains(@class,'in-sidebar-wrapper__opened')]//*[normalize-space(text())='{}']"
    OPTIMIZE_SUBMENU = (By.XPATH, MENU_SELECTOR.format("Optimize"))
    INSTORY = (By.XPATH, MENU_SELECTOR.format("InStory"))
    TEST_CAMPAIGN_NAME = ('emre' + str(test_number))

    def select_instory(self):
        self.click_element(*self.SLIDE_MENU_ICON)
        sleep(1)
        self.click_element(*self.OPTIMIZE_SUBMENU)
        sleep(1)
        self.click_element(*self.INSTORY)
        sleep(1)

    def create_campaign(self):
        sleep(1)
        self.click_element(*self.CAMPAIGN_CREATE_BUTTON)
        self.send_text(self.TEST_CAMPAIGN_NAME, *self.CAMPAIGN_NAME_INPUT)
        self.click_element(*self.CAMPAIGN_PLATFORM_TYPE_SELECTION)
        self.click_element(*self.CAMPAIGN_CREATE_CONFIRM)
        sleep(2)
        self.click_element(*self.NEXT_BUTTON)
