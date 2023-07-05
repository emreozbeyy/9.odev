from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email')
    PASS_INPUT = (By.ID, 'password')
    LOG_IN_BTN = (By.ID, 'login-button')

    def fill_login_form(self, email, password):
        self.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.find_element(*self.PASS_INPUT).send_keys(password)

    def click_login_btn(self):
        self.click_element(*self.LOG_IN_BTN)
