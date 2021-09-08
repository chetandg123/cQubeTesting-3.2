import time

from Data.parameters import Data
from reuse_func import GetData


class click_on_hyperlink():
    def __init__(self,driver):
        self.driver = driver

    def test_link(self):
        self.p = GetData()
        count = 0
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_block).click()
        time.sleep(3)
        value = self.driver.find_elements_by_class_name(Data.dots)
        total = len(value) -1
        if total != 0:
            print("Block level markers are loaded on the map ")
        else:
            print("Markers are not loaded ")
            count = count + 1
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        if total != len(value):
            print("Hyperlink is working ")
        else:
            print("Hyper link is not working ")
            count = count + 1
        return count

