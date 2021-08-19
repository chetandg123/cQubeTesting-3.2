from Data.parameters import Data
from reuse_func import GetData


class cQube_landing_page():
    def __init__(self,driver):
        self.driver = driver

    def test_SAR(self):
        self.cal = GetData()
        count=0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.attendance).click()
        if 'attendance-dashboard' not in self.driver.current_url:
            print("Attendance Dashboard is not displayed")
            count = count+1
        else:
            print("Attendance Dashboard is displayed...")
            self.cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.studentattendance).click()
            if "student-attendance" in self.driver.current_url:
                print("Navigated to Student attendance report")
            else:
                print("Student attendance report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_CRC(self):
        count=0
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.crc_visit).click()
        if 'crc-dashboard' not in self.driver.current_url:
            print("CRC Report Dashboard is not displayed")
            count = count + 1
        else:
            print("CRC Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.crcreport)
            if "crc-report" in self.driver.current_url:
                print("Navigated to  CRC report")
            else:
                print("CRC report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count




    def test_TAR(self):
        count=0
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.attendance).click()
        if 'teacher-dashboard' not in self.driver.current_url:
            print("Teacher Report Dashboard is not displayed")
            count = count + 1
        else:
            print("teacher Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.teacherattendance).click()
            if "teacher-attendance" in self.driver.current_url:
                print("Navigated to  Teacher coming soon page ")
            else:
                print(" Teacher coming soon page is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_school_map(self):
        count=0
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.sch_infra).click()
        if 'infrastructure-dashboard' not in self.driver.current_url:
            print("School infrastructure Report Dashboard is not displayed")
            count = count + 1
        else:
            print("infrastructure-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.inframap).click()
            if "school-infra-map" in self.driver.current_url:
                print("Navigated to  School infrastructure map based report")
            else:
                print("School infra map based report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count



    def test_telemetry_report(self):
        self.cal = GetData()
        count=0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Telemetry).click()
        if 'telemetry-dashboard' not in self.driver.current_url:
            print("telemetry  Report Dashboard is not displayed")
            count = count + 1
        else:
            print("telemetry-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.tele_report).click()
            self.cal.page_loading(self.driver)
            if "telemetry" in self.driver.current_url:
                print("Navigated to Telemetry report")
            else:
                print("Telemetry report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_semester_exception(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception Dashboard is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.semesterexception).click()
            self.cal.page_loading(self.driver)
            if "sem-exception" in self.driver.current_url:
                print("Navigated to Semester Exception report")
            else:
                print(" Semester Exception  report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_completionerror(self):
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        count = 0
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.Exception_Reports).click()
        if 'exception-dashboard' not in self.driver.current_url:
            print("exception-dashboard  is not displayed")
            count = count + 1
        else:
            print("exception-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.isData).click()
            self.cal.page_loading(self.driver)
            if "download-missing-data" in self.driver.current_url:
                print("Navigated to completion error data page")
            else:
                print("completion error data page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_udise_report(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.sch_infra).click()
        if 'infrastructure-dashboard' not in self.driver.current_url:
            print("Udise Dashboard is not displayed")
            count = count + 1
        else:
            print("UDISE-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.udise).click()
            self.cal.page_loading(self.driver)
            if "udise-report" in self.driver.current_url:
                print("Navigated to udise report home page")
            else:
                print("udise report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_periodic_map_report(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'sat-dashboard' not in self.driver.current_url:
            print("sat Dashboard is not displayed")
            count = count + 1
        else:
            print("sat-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.satmap).click()
            self.cal.page_loading(self.driver)
            if "pat-report" in self.driver.current_url:
                print("Navigated to peirodic map report home page")
            else:
                print("periodic map report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count


    def test_composite_metrics_report(self):
        self.cal = GetData()
        count=0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.composite_metrics).click()
        if 'composite-dashboard' not in self.driver.current_url:
            print("composite metrics Dashboard is not displayed")
            count = count + 1
        else:
            print("composite-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.composite_metric).click()
            if "composite-report" in self.driver.current_url:
                print("Navigated to Composite metrics report home page")
            else:
                print("Composite report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count