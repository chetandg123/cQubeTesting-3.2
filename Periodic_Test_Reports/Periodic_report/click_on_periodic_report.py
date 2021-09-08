import time

from Data.parameters import Data
from reuse_func import GetData


class Pat_Report_icon():
    def __init__(self, driver):
        self.driver = driver

    def check_landing_page(self):
        self.data = GetData()
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(2)
        self.data.navigate_to_periodic_report()
        self.data.page_loading(self.driver)
        if 'pat-report' in self.driver.current_url:
            print('Navigated to Periodic Assessment report')
        else:
            print('Pat report icon is not working')
            count = count + 1
        return count



