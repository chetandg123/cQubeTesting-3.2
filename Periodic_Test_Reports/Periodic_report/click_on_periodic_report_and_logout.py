import time

from Data.parameters import Data


class Logout():
    def __init__(self, driver):
        self.driver = driver

    def click_on_logout(self):
        self.driver.find_element_by_id(Data.cQube_logo).click()
        time.sleep(1)
        self.driver.find_element_by_id(Data.logout).click()
        return self.driver.title



