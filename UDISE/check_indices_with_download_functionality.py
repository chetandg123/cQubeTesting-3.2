import csv
import os
import time

from selenium.webdriver.support.select import Select

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class udiseindices_scores():
    def __init__(self,driver):
        self.driver = driver

    def infrastructure_score(self):
        self.cal = GetData()
        self.fname = file_extention()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        self.driver.find_element_by_css_selector('p >span').click()
        self.cal.page_loading(self.driver)
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(1)
        time.sleep(3)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Infrastructure score having no data found')
            return 1
        else:
            self.cal.page_loading(self.driver)
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(4)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Infrastructure_Score_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            print(self.filename)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("infrastructure_score  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1


    def administation(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(2)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print(chooseinfra.first_selected_option.text  , 'having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Administration_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Administration is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def artslab(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(3)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('artslab having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Arts_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("artslab  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def community(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(4)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Community having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(3)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Community_Participation_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Community  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def Enrollment(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(5)
        time.sleep(2)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Enrollment having no data found')
            pass
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/" + 'UDISE_report_' + management + '_Enrollment_allDistricts_' + self.cal.get_current_date() + '.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt') as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Enrollment  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
            return row_count - 1


    def grant_expenditure(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(6)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print(' Grant having no data found')
            pass
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Grant_Expenditure_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Grant expenditure is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def ictlab(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(7)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('ICTlab having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_ICT_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("ICTlab  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def Medical(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(8)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Medical having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Medical_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Medical is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def nsqf(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(9)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('nsqf having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_NSQF_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("nsqf is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1
    def policy(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(10)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Policy having no data found')
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Policy_Implementation_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Policy is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def Safety(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(11)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Safety having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Safety_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Safety  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def School_infrastructure(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(12)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('School infrastructure having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Infrastructure_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("School infrastructure is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def School_inspection(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(13)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('school inspection having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Inspection_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("school inspection  is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def School_perfomance(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(14)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('School performance having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_School_Performance_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("School performance is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def Science_lab(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(15)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Science lab having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Science_Lab_Index_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Science lab is selected and csv file is downloaded")
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1

    def Teacher_profile(self):
        self.cal = GetData()
        management = self.driver.find_element_by_id('name').text
        management = management[16:].lower().strip()
        chooseinfra = Select(self.driver.find_element_by_id('choose_infra'))
        chooseinfra.select_by_index(16)
        self.cal.page_loading(self.driver)
        if "No data found" in self.driver.page_source:
            self.driver.find_element_by_xpath(Data.hyper_link).click()
            print('Teachers profile having no data found')
            return 1
        else:
            self.driver.find_element_by_id(Data.Download).click()
            time.sleep(2)
            p = pwd()
            self.filename = p.get_download_dir() + "/"+'UDISE_report_'+management+'_Teacher_Profile_allDistricts_'+self.cal.get_current_date()+'.csv'
            time.sleep(2)
            file = os.path.isfile(self.filename)
            if True != file:
                print('csv file not downloaded')
            else:
                row_count = 0
                with open(self.filename, 'rt')as f:
                    reader = csv.reader(f)
                    data = list(reader)
                    row = len(data)
                    row_count = row
                os.remove(self.filename)
                print("Teachers profile is selected and csv file is downloaded")
                time.sleep(2)
                self.driver.find_element_by_xpath(Data.hyper_link).click()
                return row_count - 1



