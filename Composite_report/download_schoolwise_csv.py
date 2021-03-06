import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class school_wise_download():
    def __init__(self,driver):
        self.driver = driver

    def test_schoolwise(self):
        self.cal = GetData()
        self.fname = file_extention()
        self.driver.find_element_by_xpath(Data.hyper).click()
        self.cal.page_loading(self.driver)
        p =pwd()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        dist =Select(self.driver.find_element_by_name('myDistrict'))
        dist.select_by_index(1)
        self.cal.page_loading(self.driver)
        blk = Select(self.driver.find_element_by_name('myBlock'))
        blk.select_by_index(1)
        self.cal.page_loading(self.driver)
        clu = Select(self.driver.find_element_by_name('myCluster'))
        clu.select_by_index(1)
        value = self.driver.find_element_by_name('myCluster').get_attribute('value')
        value = value[3:]+'_'
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(5)
        self.cal.page_loading(self.driver)
        self.filename = p.get_download_dir() + "/" + self.fname.composite_clusterwise()+management+"_"+'schools_of_cluster_'+value.strip()+self.cal.get_current_date()+'.csv'
        print(self.filename)
        self.cal.page_loading(self.driver)
        return os.path.isfile(self.filename)

    def remove_file(self):
        os.remove(self.filename)


