import time

from Data.parameters import Data
from reuse_func import GetData


class loading_crc():
    def __init__(self,driver):
        self.driver = driver

    def test_crc(self):
        self.p = GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.p.navigate_to_crc_report()
        self.p.page_loading(self.driver)

