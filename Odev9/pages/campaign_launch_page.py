from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignLaunchPage(BasePage):
    PERSONALIZATION_LANGUAGE = (By.ID, "personalization-language")
    SELECT_LANGUAGE_OPTION = (By.CLASS_NAME, "personalization-language-all-languages")
    DATE_PICKER = (By.CLASS_NAME, "in-date-picker-wrapper_grey")  # [0]
    START_TIME = (By.XPATH, '//*[@name="startHour"]')
    DISPLAY_SETTINGS = (By.CLASS_NAME, "in-accordion-wrapper__text")  # [0]
    DISPLAY_DAYS = (By.XPATH, "//*[@for = 'When active, display the personalization only on selected days.']")  # [1]
    ACTIVE_ON_DAY_MONDAY = (By.XPATH, "//*[@value= 'Monday']")  # Tuesday #Friday
    ACTIVE_ON_DAY_TUESDAY = (By.XPATH, "//*[@value= 'Tuesday']")
    ACTIVE_ON_DAY_WEDNESDAY = (By.XPATH, "//*[@value= 'Wednesday']")
    ACTIVE_ON_DAY_THURSDAY = (By.XPATH, "//*[@value= 'Thursday']")
    ACTIVE_ON_DAY_FRIDAY = (By.XPATH, "//*[@value= 'Friday']")  # Tuesday #Friday
    ADVANCE_SETTINGS = (By.CLASS_NAME, "in-accordion-wrapper__text")  # [1]
    PRIORITY = (By.ID, "priority")
    PRIORITY_SELECTION = (By.CLASS_NAME, "priority-7")
    ACTIVE_MODE_SELECTION = (By.XPATH, '//*[@for="Test"]')
    ADD_NOTE = (By.ID, "note")
    NEXT_BUTTON = (By.ID, "save-and-next")
    NOTE = 'Test Note'

    def campaign_launch_step(self):
        self.wait_for_element_clickable(self.PERSONALIZATION_LANGUAGE).click()
        self.wait_for_element_clickable(self.SELECT_LANGUAGE_OPTION).click()
        self.wait_for_element_clickable(self.DATE_PICKER).click()
        sleep(2)
        self.send_text(1630, *self.START_TIME)
        self.scroll_execute_script()
        self.all_elements_located(self.DISPLAY_SETTINGS)[0].click()
        self.element_located(self.DISPLAY_DAYS).click()
        self.wait_for_element_clickable(self.ACTIVE_ON_DAY_MONDAY).click()
        self.wait_for_element_clickable(self.ACTIVE_ON_DAY_TUESDAY).click()
        self.wait_for_element_clickable(self.ACTIVE_ON_DAY_WEDNESDAY).click()
        self.wait_for_element_clickable(self.ACTIVE_ON_DAY_THURSDAY).click()
        self.wait_for_element_clickable(self.ACTIVE_ON_DAY_FRIDAY).click()
        sleep(2)
        self.scroll_execute_script()
        self.all_elements_located(self.ADVANCE_SETTINGS)[1].click()
        sleep(2)
        self.visibility_of_element(self.PRIORITY).click()
        self.element_located(self.PRIORITY_SELECTION).click()
        self.wait_for_element_clickable(self.ACTIVE_MODE_SELECTION).click()
        self.send_text(self.NOTE, *self.ADD_NOTE, )
        self.wait_for_element_clickable(self.NEXT_BUTTON).click()
        sleep(2)
