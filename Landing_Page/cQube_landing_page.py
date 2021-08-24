import unittest
from Landing_Page.cQube_icons import cQube_landing_page
from reuse_func import GetData

class cQube_Home(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(50)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)


    def test_sar_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_SAR()
        self.data.page_loading(self.driver)

    def test_crc_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_crc_visit_report()
        self.assertEqual(0,result,msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_semester_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_Semester_map()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_semester_heatchart_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_Semester_heatchart()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)


    def test_tar_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_TAR()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_school_map_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_school_infrastructure_map()
        self.data.page_loading(self.driver)
    #
    def test_school_chart_icon(self):
        b =cQube_landing_page(self.driver)
        result = b.test_composite_chart_map()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)


    def test_sem_exception(self):
        b = cQube_landing_page(self.driver)
        res = b.check_semester_Exception_report_icon()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_telemetry_icon(self):
        b = cQube_landing_page(self.driver)
        result = b.check_telemetry_icon()
        self.assertEqual(0, result, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_completionerror(self):
        b = cQube_landing_page(self.driver)
        res = b.check_isdata_exception_list()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_composite_metrics_Report(self):
        b = cQube_landing_page(self.driver)
        res = b.check_composite_metrics()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_patreport(self):
        b = cQube_landing_page(self.driver)
        res = b.test_periodic_map_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_pat_heatchart_report(self):
        b = cQube_landing_page(self.driver)
        res = b.test_periodic_heatchart_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_pat_lo_report(self):
        b = cQube_landing_page(self.driver)
        res = b.test_periodic_lo_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)

    def test_udisereport(self):
        b = cQube_landing_page(self.driver)
        res = b.test_udise_report()
        self.assertEqual(0, res, msg='Report page is not exist')
        self.data.page_loading(self.driver)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()