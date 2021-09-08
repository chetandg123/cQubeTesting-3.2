import time
from selenium.webdriver.support.select import Select
from Data.parameters import Data
from reuse_func import GetData


class Homeicon():
   def __init__(self,driver):
       self.driver = driver

   def test_homeicon(self):
       self.p =GetData()
       count = 0
       self.driver.implicitly_wait(20)
       self.driver.find_element_by_xpath(Data.hyper_link).click()
       self.p.page_loading(self.driver)
       dist = Select(self.driver.find_element_by_name("myDistrict"))
       dist.select_by_index(1)
       self.p.page_loading(self.driver)
       distname = dist.options[1].text
       print(distname)
       self.driver.find_element_by_xpath(Data.hyper_link).click()
       time.sleep(2)
       self.p.page_loading(self.driver)
       if distname == dist.first_selected_option.text:
           print("Hyperlink is not working....")
           count = count + 1
       else:
           pass
       return count

   def test_homebutton(self):
       self.p = GetData()
       count = 0
       self.driver.implicitly_wait(20)
       self.driver.find_element_by_xpath(Data.hyper).click()
       self.p.page_loading(self.driver)
       self.driver.find_element_by_id(Data.cQube_logo).click()
       self.p.page_loading(self.driver)
       if 'dashboard' in self.driver.current_url:
           print("home button is working fine , landing page is displayed ")
       else:
           print("Landing page is not displayed due to cQube logo click not happened")
           count = count + 1
       self.p.navigate_to_crc_report()
       self.p.page_loading(self.driver)
       return count