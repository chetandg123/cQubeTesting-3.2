# from selenium import webdriver
#
# from get_dir import pwd
#
# p = pwd()
#
# driver = webdriver.Chrome(executable_path= p.get_driver_path())
# str1 = driver.capabilities['browserVersion']
# str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
# print(str1)
# print(str2)
# print(str1[0:2])
# print(str2[0:2])
# if str1[0:2] != str2[0:2]:
#   print("please download correct chromedriver version")
import pandas as pd

from get_dir import pwd

p = pwd()
filename ="/home/chetan/Documents/cQube/cQubeTesting-3.0/Downloads/periodic_assesment_test_govt_2021-22_October_allGrades__schools_of_cluster_2424050001_19-10-2021.csv"
df = pd.read_csv(filename , usecols =["Total Students","Students Attended","Total Schools"])
print(df)

student = df['Total Students'].sum()
# print(student)





school = int(df['Total Schools'].sum())
students = df['Total Students'].sum()
attend = df['Students Attended'].sum()
print(type(school))
