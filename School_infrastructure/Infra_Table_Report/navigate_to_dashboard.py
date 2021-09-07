import time

from Data.parameters import Data
from reuse_func import GetData


class check_dashboard():
    def __init__(self,driver):
        self.driver = driver

    def test_menulist(self):
        self.p = GetData()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.sch_infra).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.composite).click()
        self.p.page_loading(self.driver)
