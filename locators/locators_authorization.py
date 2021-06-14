from selenium.webdriver.common.by import By


class LocatorsAuthorization(object):
    '''Локаторы, которые относятся к странице авторизации'''
    INPUT_EMAIL_MAIN = (By.ID, "2email")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "2password")
    REMEMBER_ME = (By.XPATH, "//label[@class='description']")
    FORGOT = (By.ID, "forgot")
    ENTRANCE = {
        'ru': (By.XPATH, "//button[text()='Войти']"),
        'en': (By.XPATH, "//button[text()='Sign in']")
    }
    OPEN_LIST_LANGUAGE = (By.ID, "language-list")
    SELECT_LANGUAGE_INACTIVE = {
        'en': (By.XPATH, "//span[.='English']"),
        'ru': (By.XPATH, "//span[.='Русский']")
    }
    EMAIL_ERROR = (By.ID, "2email-error")
    PASSWORD_ERROR = (By.ID, "pass-error")
    REGISTRATION = (By.XPATH, "//div[@class='registration']/a")
    SEND_INSTRUCTION = {
        'en': (By.XPATH, "//*[contains(text(), 'Send instruction')]"),
        'ru': (By.XPATH, "//*[contains(text(), 'Выслать инструкцию')]")
    }
    SEND_STOP = {
        'en': (By.XPATH, "//*[contains(text(), 'Cancel')]"),
        'ru': (By.XPATH, "//*[contains(text(), 'Отмена')]")
    }
    ERROR_LOGIN_OR_PASSWORD = (By.XPATH, "//div[@class='red']")
