from steps.base_page import *
from locators.locators_authorization import LocatorsAuthorization
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Authorization(BasePage):

    def input_email_main(self, text):
        self.driver.find_element(*LocatorsAuthorization.INPUT_EMAIL_MAIN).send_keys(text)

    def check_input_email_main(self, text):
        email = self.driver.find_element(*LocatorsAuthorization.INPUT_EMAIL_MAIN).get_attribute('value')
        assert email == text, f'Поля не сходятся {email} != {text}'

    def input_password(self, password):
        self.driver.find_element(*LocatorsAuthorization.INPUT_PASSWORD).send_keys(password)

    def click_sign_in(self, lang):
        self.driver.find_element(*LocatorsAuthorization.ENTRANCE[lang]).click()

    def click_remember_me(self):
        self.driver.find_element(*LocatorsAuthorization.REMEMBER_ME).click()

    def click_registration(self):
        self.driver.find_element(*LocatorsAuthorization.REGISTRATION).click()

    def click_forgot(self):
        self.driver.find_element(*LocatorsAuthorization.FORGOT).click()

    def input_email_forgot(self, text):
        self.driver.find_element(*LocatorsAuthorization.INPUT_EMAIL).send_keys(text)

    def check_input_email_forgot(self, text):
        email = self.driver.find_element(*LocatorsAuthorization.INPUT_EMAIL).get_attribute('value')
        assert email == text, f'Поля не сходятся {email} != {text}'

    def click_send_instruction(self, lang):
        self.driver.find_element(*LocatorsAuthorization.SEND_INSTRUCTION[lang]).click()

    def check_error_email(self):
        self.driver.find_element(*LocatorsAuthorization.EMAIL_ERROR)  # Можно использовать явное ожидание

    def check_error_password(self):
        self.driver.find_element(*LocatorsAuthorization.PASSWORD_ERROR)

    def check_error_or_password(self):
        self.driver.find_element(*LocatorsAuthorization.ERROR_LOGIN_OR_PASSWORD)
