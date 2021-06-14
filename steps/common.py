from steps.base_page import *


class Common(BasePage):

    def find_text(self, text):
        self.driver.find_element_by_xpath(f"//*[text()='{text}']")

    def open_url(self, url):
        self.driver.get(url)
