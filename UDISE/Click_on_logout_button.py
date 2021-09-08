import time

from selenium.common import exceptions

from Data.parameters import Data
from reuse_func import GetData


class click_on_logout():
    def __init__(self,driver):
        self.driver =driver
    def test_logout(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        print("Logout button is working as expected ")
        self.p.page_loading(self.driver)
        return self.driver.title


