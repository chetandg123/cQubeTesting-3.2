import time

from Data.parameters import Data
from reuse_func import GetData


class Check_order_of_tabledata():
    def __init__(self,driver):
        self.driver = driver
    def test_order(self):
        self.p =GetData()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath("//th[contains(text(),'District Name')]").click()
        self.p.page_loading(self.driver)
        values = self.driver.find_elements_by_class_name("sorting sorting_asc")
        for i in values:
            print(i.get_attribute("aria-sort"))

        self.p.page_loading(self.driver)
        self.driver.find_element_by_xpath("//th[contains(text(),'District Name')]").click()
        self.p.page_loading(self.driver)
        value = self.driver.find_elements_by_class_name("sorting sorting_desc")
        for i in value:
            print(i.get_attribute("aria-sort"))

        self.driver.find_element_by_xpath(Data.hyper).click()
        self.p.page_loading(self.driver)
        return len(value)

