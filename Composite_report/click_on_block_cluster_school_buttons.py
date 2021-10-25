import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from reuse_func import GetData


class Blocks_cluster_schools_Buttons():
    def __init__(self,driver):
        self.driver = driver

    def click_on_blocks_button(self):
        count = 0
        self.data  = GetData()
        self.driver.refresh()
        time.sleep(4)
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('allBlock').click()
        time.sleep(3)
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Block level graph is not displayed ")
            count = count + 1
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        for i in range(1,len(xaxis_lists.options)-10):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        yaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        for i in range(1,len(yaxis_lists.options)-10):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        return count

    def click_on_clusters_button(self):
        count = 0
        self.data  = GetData()
        self.driver.find_element_by_xpath(Data.hyper_link).click()
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id('allCluster').click()
        self.data.page_loading(self.driver)
        graph = self.driver.find_element_by_id('myChart')
        result = graph.is_displayed()
        if True != result:
            print("Cluster level graph is not displayed ")
            count = count + 1
        xaxis_lists = Select(self.driver.find_element_by_id('x_axis'))
        for i in range(1,len(xaxis_lists.options)-10):
            time.sleep(2)
            xaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        yaxis_lists = Select(self.driver.find_element_by_id('y_axis'))
        for i in range(1,len(yaxis_lists.options)-10):
            time.sleep(2)
            yaxis_lists.select_by_index(i)
            self.data.page_loading(self.driver)
        return count




