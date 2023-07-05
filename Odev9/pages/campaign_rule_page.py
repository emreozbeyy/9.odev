import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CampaignRulePage(BasePage):
    SELECT_RULE = (By.XPATH, './/*[contains(@class, "page-rule")]')
    RULE_CONDITION_LIST = (By.XPATH, '//button[@data-title="Cart Amount"]')
    CONDITION_LIST_SELECT_PAGE_TYPE = (By.CLASS_NAME, "conditionList0-page-type")
    NEXT_BUTTON = (By.ID, "save-and-next")
    CONDITION_LIST = (By.ID, 'conditionList0')
    CONDITION_SEARCH_BOX = (By.ID, 'conditionList0-search')
    OPERATOR_LIST = (By.ID, 'operatorList0')
    OPERATOR_SELECTION = "//*[contains(@class, 'in-dropdown')]//a[text() = ' {} ']"

    condition = "Page Type"
    operator = "is"

    def campaign_rule_step(self):
        self.wait_for_element_clickable(self.SELECT_RULE)
        time.sleep(1)
        self.click_element(*self.SELECT_RULE)
        self.select_condition(self.condition).select_operator(self.operator)
        self.click_save_and_continue()

    def select_condition(self, condition):
        self.wait_for_element_clickable(self.CONDITION_LIST).click()
        self.fill(condition, *self.CONDITION_SEARCH_BOX).fill(Keys.ENTER, *self.CONDITION_SEARCH_BOX)
        return self

    def select_operator(self, operator):
        self.click(*self.OPERATOR_LIST)
        self.click(By.XPATH, self.OPERATOR_SELECTION.format(operator))

    def click_save_and_continue(self):
        time.sleep(1)
        self.wait_for_element_clickable(self.NEXT_BUTTON).click()

        return self
