
import unittest

from CRC import crc_report_smoke_testing
from Diksha_Reports.content_course import content_course_smoke_testing
from Diksha_Reports.content_textbook import content_textbook_smoke_suite
from Diksha_Reports.usage_by_course import usage_by_course_smoke_testing
from Diksha_Reports.usage_by_textbook import usage_by_textbook_smoke_suite
from Diksha_TPD.TPD_Completion_percentage import completion_smoke_test
from Diksha_TPD.TPD_Course_Progress import lpd_content_smoke_test
from Diksha_TPD.TPD_Enrollment_completion import enrollment_smoke_test
from Diksha_TPD.TPD_Teacher_Percentage import lpd_percentage_smoke_test

from Health_Card_Index import health_card_smoke_test
from School_infrastructure.Infra_Table_Report import School_report_smoke_testing

from get_dir import pwd
from reuse_func import GetData
from HTMLTestRunner import HTMLTestRunner


class MyTestSuite_smoke_chart_tables(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.data = GetData()
        self.driver = self.data.get_driver()
        self.driver.implicitly_wait(100)
        self.data.open_cqube_appln(self.driver)
        self.data.login_cqube(self.driver)
        self.data.page_loading(self.driver)

    # def test_issue01(self):
    #
    #         smoke_test = unittest.TestSuite()
    #         smoke_test.addTests([
    #             unittest.defaultTestLoader.loadTestsFromTestCase(
    #                 patheatchart_smoke_test.cQube_heatchart_Smoke_test
    #                 )
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_smoke_chart_tables_report(), "w")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title=' PAT Heat chart Infra_Table_Report Smoke Test Infra_Table_Report',
    #             verbosity=1,
    #
    #         )
    #         runner1.run(smoke_test)
    #         outfile.close()
    #
    # def test_issue02(self):
    #
    #         smoke_test = unittest.TestSuite()
    #         smoke_test.addTests([
    #             unittest.defaultTestLoader.loadTestsFromTestCase(
    #                 PAT_LO_Table_smoke_suite.cQube_pat_lotable_smoke_test
    #               )
    #         ])
    #         p = pwd()
    #         outfile = open(p.get_smoke_chart_tables_report(), "a")
    #
    #         runner1 = HTMLTestRunner.HTMLTestRunner(
    #             stream=outfile,
    #             title=' PAT LO Table Infra_Table_Report Smoke Test Infra_Table_Report',
    #             verbosity=1,
    #
    #         )
    #         runner1.run(smoke_test)
    #         outfile.close()
    #
    def test_issue03(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                content_course_smoke_testing.cQube_content_course_smoke)
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content BY Course Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue04(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    content_textbook_smoke_suite.cQube_content_textbook_smoke
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Content By Textbook report Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue05(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_course_smoke_testing.cQube_diskha_course_smoke_test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Course Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue06(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    usage_by_textbook_smoke_suite.cQube_usage_textbook_smoke_report
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' Usage By Textbook  Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue07(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    lpd_content_smoke_test.cQube_lpdcontent_smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' TPD Content Progress  Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue08(self):

            smoke_test = unittest.TestSuite()
            smoke_test.addTests([
                unittest.defaultTestLoader.loadTestsFromTestCase(
                    lpd_percentage_smoke_test.cQube_tpd_percentage_smoke_Test
                )
            ])
            p = pwd()
            outfile = open(p.get_smoke_chart_tables_report(), "a")

            runner1 = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=' TPD Percentage Progress  Smoke Test Infra_Table_Report',
                verbosity=1,

            )
            runner1.run(smoke_test)
            outfile.close()

    def test_issue09(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                enrollment_smoke_test.cQube_enrollment_smoketest
            )
        ])
        p = pwd()
        outfile = open(p.get_smoke_chart_tables_report(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=' TPD Enrollment/Completion Smoke Test Infra_Table_Report',
            verbosity=1,

        )
        runner1.run(smoke_test)
        outfile.close()

    def test_issue10(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(
                completion_smoke_test.cQube_completion_percentage_smoke
            )
        ])
        p = pwd()
        outfile = open(p.get_smoke_chart_tables_report(), "a")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='TPD Completion Percentage Smoke Test Infra_Table_Report',
            verbosity=1,

        )
        runner1.run(smoke_test)
        outfile.close()

    # def test_issue11(self):
    #     smoke_test = unittest.TestSuite()
    #     smoke_test.addTests([
    #         unittest.defaultTestLoader.loadTestsFromTestCase(
    #             health_card_smoke_test.Health_card_smoke_test
    #
    #         )
    #     ])
    #     p = pwd()
    #     outfile = open(p.get_smoke_chart_tables_report(), "w")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title='Health card Infra_Table_Report Smoke Test Infra_Table_Report',
    #         verbosity=1,
    #
    #     )
    #     runner1.run(smoke_test)
    #     outfile.close()

    # def test_issue13(self):
    #     smoke_test = unittest.TestSuite()
    #     smoke_test.addTests([
    #         # file name .class name
    #         unittest.defaultTestLoader.loadTestsFromTestCase(crc_report_smoke_testing.cQube_CRC_Report),
    #     ])
    #     p = pwd()
    #     outfile = open(p.get_smoke_chart_tables_report(), "a")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title='Crc Test Infra_Table_Report',
    #         verbosity=1,
    #
    #     )
    #
    #     runner1.run(smoke_test)
    #     outfile.close()

    # def test_issue14(self):
    #     smoke_test = unittest.TestSuite()
    #     smoke_test.addTests([
    #         unittest.defaultTestLoader.loadTestsFromTestCase(School_report_smoke_testing.cQube_SI_Report)
    #     ])
    #     p = pwd()
    #     outfile = open(p.get_smoke_chart_tables_report(), "a")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title='School Infra Infra_Table_Report',
    #         verbosity=1,
    #
    #     )
    #
    #     runner1.run(smoke_test)
    #     outfile.close()

    # def test_issue15(self):
    #     smoke_test = unittest.TestSuite()
    #     smoke_test.addTests([
    #         unittest.defaultTestLoader.loadTestsFromTestCase(
    #             composite_smoke_testing.composite_smoke_testing)
    #     ])
    #     p = pwd()
    #     outfile = open(p.get_smoke_chart_tables_report(), "a")
    #
    #     runner1 = HTMLTestRunner.HTMLTestRunner(
    #         stream=outfile,
    #         title='Composite Infra_Table_Report smoke Test Infra_Table_Report',
    #         verbosity=1,
    #
    #     )
    #
    #     runner1.run(smoke_test)
    #     outfile.close()
    @classmethod
    def tearDownClass(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()