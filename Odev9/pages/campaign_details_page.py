import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignDetailsPage(BasePage):
    DETAILS = (By.CLASS_NAME, "details")
    CLOSE_BUTTON = (By.CLASS_NAME, "qa-close")
    PRIORTY_VALUE = 'priority-value'
    PAGE_RULE_VALUE = 'personalization-rule-0'
    NOTE_VALUE = 'personalization-note'
    TEST_LINK = (By.XPATH, '//td[contains(@class, "test-link")]')
    TEST_LINKS_LIST = (By.CLASS_NAME, "test-link-wrapper")
    FIRST_LINKS = (By.CSS_SELECTOR, ".in-box .clearfix")  # [0]
    VARIANT_SELECTION = "dropDownList"
    VARIANT_DOMAIN_SELECTION = (By.CSS_SELECTOR, ".in-box .clearfix a")
    CAMPAIGN_VISIBILITY = '//*[@class = "inspector-personalization-visibility inspector-personalization-visible"]'
    CAMPAIGN_DETAILS = (By.XPATH, "//*[contains(@class, 'vuetable-body')]//*[contains(text(), 'Details')]")
    CAMP_NAME = (By.CLASS_NAME, 'in-modal-wrapper__title')
    CAMP_PRIORITY = (By.ID, 'priority-value')
    CAMP_RULES = (By.CLASS_NAME, 'personalization-rule-0')
    CAMP_NOTE = (By.CLASS_NAME, 'personalization-note')
    DETAIL_CLOSE = (By.CLASS_NAME, 'qa-close')
    TEST_LINK_VARIATION_GROUP_BTNS = (By.CSS_SELECTOR, '.in-box .clearfix')
    TEST_LINK_DOMAIN_URL = (By.CSS_SELECTOR, '.in-box .clearfix a')
    CAMPAIGN_ID = (By.ID, 'i-d-value')

    def go_to_campaign_details(self):
        self.wait_for_element_clickable(self.CAMPAIGN_DETAILS).click()
        camp_id = self.visibility_of_element(self.CAMPAIGN_ID).text
        return camp_id

    def get_campaign_name(self):
        return self.visibility_of_element(self.CAMP_NAME).text

    def get_campaign_priority(self):
        return self.visibility_of_element(self.CAMP_PRIORITY).text

    def get_campaign_rules(self):
        return self.visibility_of_element(self.CAMP_RULES).text

    def get_campaign_note(self):
        return self.visibility_of_element(self.CAMP_NOTE).text

    def click_test_link(self):
        self.wait_for_element_clickable(self.TEST_LINK).click()

    def campaign_open_test_link_step(self):
        self.click_test_link()
        self.visibility_of_element(self.FIRST_LINKS)
        self.hover_move_to_element(*self.FIRST_LINKS)
        time.sleep(2)
        self.incognito(self.find_elements(0, *self.VARIANT_DOMAIN_SELECTION).get_attribute('href'))

    def close_detail_side_menu(self):
        self.click_element(*self.DETAIL_CLOSE)
