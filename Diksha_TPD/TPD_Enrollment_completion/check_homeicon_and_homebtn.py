import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from get_dir import pwd
from reuse_func import GetData


class Home_functionalities():
    def __init__(self,driver):
        self.driver = driver

    def test_homeicon_functionality(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 30 Days ')
        timeseries.select_by_index(2)
        self.data.page_loading(self.driver)
        # present = self.driver.find_element_by_id(Data.homeicon).isDisplayed()
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.navigate_to_tpd_enrollment_report()
        print('checked with cQube logo function is working ')
        self.data.page_loading(self.driver)
        # return  present

    def test_homebtn_funtion(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        self.data.page_loading(self.driver)
        if 'dashboard' in self.driver.current_url:
            print('cQube logo functionality is working ')
        else:
            print('cQube logo is not working ')
            count = count + 1
        self.data.page_loading(self.driver)
        self.data.navigate_to_tpd_enrollment_report()
        self.data.page_loading(self.driver)
        return  count

    def test_hyperlink_function(self):
        self.data = GetData()
        self.p = pwd()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        timeseries = Select(self.driver.find_element_by_name(Data.timeperiods))
        # timeseries.select_by_visible_text(' Last 7 Days ')
        timeseries.select_by_index(3)
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        print("Checked with hyper link function")
        time.sleep(3)
        self.data.page_loading(self.driver)


