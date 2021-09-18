import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class cluster_btn_scores():
    def __init__(self,driver):
        self.driver = driver

    def test_click_clusters(self):
        self.driver.implicitly_wait(30)
        self.p = GetData()
        count = 0
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.p.page_loading(self.driver)
        self.driver.find_element_by_id(Data.scm_cluster).click()
        time.sleep(10)
        scores = Select(self.driver.find_element_by_id("choose_infra"))
        print("no of infra scores:",len(scores.options))
        for i in range(1,len(scores.options)-1):
            time.sleep(1)
            scores.select_by_index(i)
            time.sleep(3)
            if 'No data found' in self.driver.page_source:
                print(scores.options[i].text,'showing no data found!..')
            else:
                self.p.page_loading(self.driver)
                markers = self.driver.find_elements_by_class_name(Data.dots)
                dots = len(markers) - 1
                if dots == 0:
                    print(i, 'does not contains markers on map ')
                    count = count + 1
            self.p.page_loading(self.driver)
            scores.select_by_index(1)
            time.sleep(2)
            return count