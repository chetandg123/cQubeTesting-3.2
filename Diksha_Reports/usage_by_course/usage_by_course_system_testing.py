


import unittest
from Diksha_Reports.usage_by_course.check_course_type_content_play_counts import test_course_based_on_timeperiods
from Diksha_Reports.usage_by_course.click_on_homeicon import Diksha_column_homeicon
from Diksha_Reports.usage_by_course.click_on_hyperlink import Diksha_column_hyperlink
from Diksha_Reports.usage_by_course.click_on_logout import Diksha_column_logout
from Diksha_Reports.usage_by_course.donwloading_districtlevel_file import overalldownload

from reuse_func import GetData


class cQube_diskha_course_system_report(unittest.TestCase):

    @classmethod
    def setUpClass(self):
            self.data = GetData()
            self.driver = self.data.get_driver()
            self.driver.implicitly_wait(100)
            self.data.open_cqube_appln(self.driver)
            self.data.login_cqube(self.driver)
            self.data.page_loading(self.driver)
            self.data.navigate_to_column_course()
            self.data.page_loading(self.driver)


    def test_navigation_from_hamburger(self):
        count = 0
        self.data.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.data.page_loading(self.driver)
        self.data.navigate_to_column_course()
        self.data.page_loading(self.driver)
        if 'usage-by-course' in self.driver.current_url:
            print('Home button is working')
        else:
            print("usage-by-course should be display in url ")
            count = count + 1
        self.assertEqual(0,count , msg="Navigatation to diksha couse report is failed ")
        self.data.page_loading(self.driver)


    def test_overalldownload(self):
        b = overalldownload(self.driver)
        res = b.download_csv_file()
        self.assertEqual(0,res,msg='Failed due to mismatch found on content plays')
        self.data.page_loading(self.driver)


    def test_test_course_based_on_last30days(self):
        b = test_course_based_on_timeperiods(self.driver)
        res = b.test_last30_days()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_last7days(self):
        b = test_course_based_on_timeperiods(self.driver)
        res = b.test_last7_days()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)

    def test_test_course_based_on_lastday(self):
        b = test_course_based_on_timeperiods(self.driver)
        res = b.test_last_day()
        self.assertEqual(0,res,msg='mis match found at content usage ')
        self.data.page_loading(self.driver)







    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
