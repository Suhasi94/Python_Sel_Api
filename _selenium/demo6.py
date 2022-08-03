import csv
from selenium.common.exceptions import NoSuchElementException
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("chromedriver.exe")

driver.get(r"C:\Users\singh\PycharmProjects\project1new\_selenium\sir file\demo.html")

driver.maximize_window()
sleep(3)


elements = driver.find_elements_by_xpath("//table[@name='customers']//td[2]")

actual_fnames = [element.text for element in elements]

# Get the sorted version of the actula_fnames
sorted_fnames = sorted(actual_fnames)

if actual_fnames == sorted_fnames:
    print("PASS")
else:
    print("FAIL")