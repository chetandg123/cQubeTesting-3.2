import os
import time
from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class Download_districtwise():
    def __init__(self,driver):
        self.driver = driver

    def download_all_district_records(self):
        self.p = pwd()
        self.load = GetData()
        count = 0
        self.fname = file_extention()
        self.driver.find_element_by_id(Data.home).click()
        self.load.page_loading(self.driver)
        self.load.navigate_to_heatchart_report()
        self.load.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        self.filename = self.p.get_download_dir() + '/' + self.fname.pchart_all_districts()
        if os.path.isfile(self.filename) != True:
                print("Districtwise csv file is not downloaded")
        else:
             print('District wise csv file is downloaded ')
        os.remove(self.filename)
        self.load.page_loading(self.driver)
        return count



