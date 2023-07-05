from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.campaign_start_page import CampaignStartPage


class CampaignGeneratePage(BasePage):
    USER_NAME = (By.CLASS_NAME, "router-link-active")
    GENERATE_BUTTON = (By.XPATH, "//*[contains(text(), 'Generate')]")  # [1]
    LAUNCH_ALERT_BOX = (By.CLASS_NAME, "messageAlertBox")
    SEARCH_BUTTON = (By.ID, 'search-value')
    DETAILS = (By.CLASS_NAME, "details")
    CLOSE_BUTTON = (By.CLASS_NAME, "qa-close")
    PRIORTY_VALUE = 'priority-value'
    PAGE_RULE_VALUE = 'personalization-rule-0'
    NOTE_VALUE = 'personalization-note'

    def campaign_generate_step(self):
        for count in range(2):
            self.element_located(self.USER_NAME).click()
            sleep(3)
            self.visibility_of_element(self.GENERATE_BUTTON).click()
            sleep(10)
            self.driver.refresh()

        self.send_text(CampaignStartPage.TEST_CAMPAIGN_NAME, *self.SEARCH_BUTTON, )
        sleep(3)
