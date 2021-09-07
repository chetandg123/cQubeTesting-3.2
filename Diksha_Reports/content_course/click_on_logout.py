import time

from Data.parameters import Data
from reuse_func import GetData


class content_course_logout():
    def __init__(self,driver):
        self.driver = driver

    def test_logout(self):
        self.data = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        time.sleep(2)
        loginpage = self.driver.title
        return loginpage
