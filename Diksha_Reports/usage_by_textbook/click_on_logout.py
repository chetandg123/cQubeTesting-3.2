import time

from Data.parameters import Data
from reuse_func import GetData


class Diksha_column_logout():
    def __init__(self,driver):
        self.driver = driver

    def test_logout(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        loginpage = self.driver.title
        self.data.login_cqube(self.driver)
        print("Logout button is working as expected.. now relogging to cQube ")
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_textbook()
        self.data.page_loading(self.driver)
        return loginpage
