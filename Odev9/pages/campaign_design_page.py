import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignDesignPage(BasePage):
    ADD_NEW_VARIATION = (By.ID, "add-new-variation")
    ADD_NEW_VARIANT_BUTTON = (By.ID, "add-new-variation")
    TEMPLATE_LIST = (By.CLASS_NAME, 'template-list')
    SELECT_INSTORY_TEMPLATE_BUTTON = (By.XPATH, '//*[@class="template-list"]'
                                                '//*[text()="Single Story"] /ancestor::li//*[@class="btn-select"]')
    SELECT_INSTORY_TEMPLATE = (By.XPATH, '//*[@class ="template-list"]//li//*[text()="Single Story"]')
    OKBUTTON = (By.LINK_TEXT, 'OK')
    NOTIFICATION_CONFIRM = (By.CLASS_NAME, "inline-select-notification-confirm")
    SWITCH_IFRAME = (By.XPATH, '//*[@id="iframe-edit"]')
    PARTNER_HEADER = (By.CSS_SELECTOR, 'div.top-header')
    INSERT_AFTER = (By.CLASS_NAME, 'append-after')
    SAVE_BTN = (By.CLASS_NAME, 'btn-save')
    NEXT_BUTTON = (By.ID, "save-and-next")
    TEMPLATE_LIST_ELEMENTS = 'li'
    IFRAME_EDIT = (By.ID, 'ins-skeleton-partner-iframe')
    IFRAME_SAVE = (By.ID, 'inone')
    DESIGN_BUTTON = (By.ID, 'design')

    def add_new_variation(self):
        self.wait_for_element_clickable(self.ADD_NEW_VARIATION).click()

    def select_template(self):
        time.sleep(10)
        self.visibility_of_element(self.SELECT_INSTORY_TEMPLATE)
        self.wait_for_element_clickable(self.SELECT_INSTORY_TEMPLATE)
        self.hover_move_to_element(*self.SELECT_INSTORY_TEMPLATE)
        self.visibility_of_element(self.SELECT_INSTORY_TEMPLATE_BUTTON)
        self.wait_for_element_clickable(self.SELECT_INSTORY_TEMPLATE_BUTTON)
        time.sleep(1)
        self.click_element(*self.SELECT_INSTORY_TEMPLATE_BUTTON)

    def template_ok_button(self):
        time.sleep(10)
        self.wait_for_element_clickable(self.OKBUTTON)
        time.sleep(1)
        self.click_element(*self.OKBUTTON)

    def insert_template(self):
        time.sleep(3)
        self.template_ok_button()
        time.sleep(5)
        with self.switch_frame(self.IFRAME_EDIT):
            self.wait_for_element_clickable(self.PARTNER_HEADER).click()
        self.wait_for_element_clickable(self.INSERT_AFTER).click()
        time.sleep(10)
        self.wait_for_element_clickable(self.DESIGN_BUTTON).click()
        time.sleep(5)

    def save_template(self):
        time.sleep(5)
        with self.switch_frame(self.IFRAME_SAVE):
            self.wait_for_element_clickable(self.SAVE_BTN)
            self.click_element(*self.SAVE_BTN)
