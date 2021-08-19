from Data.parameters import Data
from reuse_func import GetData


class cQube_landing_page():
    def __init__(self,driver):
        self.driver = driver

    def test_school_infrastructure_map(self):
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

    def test_composite_chart_map(self):
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
            self.driver.find_element_by_id(Data.composite).click()
            if "school-infrastructure" in self.driver.current_url:
                print("Navigated to  School infrastructure chart report")
            else:
                print("School infrastructure chart  report is not exist")
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

    def test_Semester_map(self):
        count = 0
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Report Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.satmap).click()
            if "semester-report" in self.driver.current_url:
                print("Navigated to  Semester report")
            else:
                print("Semester report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_Semester_heatchart(self):
        count = 0
        self.cal = GetData()
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Report Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard Dashboard is displayed ...")
            self.driver.find_element_by_id(Data.sat_heatchart).click()
            if "sat-heat-chart" in self.driver.current_url:
                print("Navigated to  Semester Heatchart report")
            else:
                print("Semester Heatchart report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_periodic_map_report(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.satmap).click()
            self.cal.page_loading(self.driver)
            if "pat-report" in self.driver.current_url:
                print("Navigated to peirodic map report home page")
            else:
                print("periodic map report home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_periodic_lo_report(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.patlotable).click()
            self.cal.page_loading(self.driver)
            if "PAT-LO-table" in self.driver.current_url:
                print("Navigated to PAT-LO-table home page")
            else:
                print("PAT-LO-table home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_periodic_heatchart_report(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.std_performance).click()
        if 'std-performance-dashboard' not in self.driver.current_url:
            print("std-performance-dashboard Dashboard is not displayed")
            count = count + 1
        else:
            print("std-performance-dashboard-dashboard is displayed ...")
            self.driver.find_element_by_id(Data.patheatchart).click()
            self.cal.page_loading(self.driver)
            if "heat-chart" in self.driver.current_url:
                print("Navigated to PAT heatchart home page")
            else:
                print("PAT-heatchart home page report is not exist")
            self.driver.find_element_by_id(Data.cQube_logo).click()
            self.cal.page_loading(self.driver)
        return count

    def test_SAR(self):
        self.cal = GetData()
        count = 0
        self.cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.menu_icon).click()
        self.driver.find_element_by_id(Data.attendance).click()
        if 'attendance-dashboard' not in self.driver.current_url:
            print("Attendance Dashboard is not displayed")
            count = count + 1
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

    def test_TAR(self):
        count = 0
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
