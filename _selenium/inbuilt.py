from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("file:///C:/Users/singh/PycharmProjects/project1new/_selenium/sir%20file/demo.html")
driver.maximize_window()
element = driver.find_element_by_id("standard_cars")
s = Select(element)
s.select_by_index(4)
sleep(2)
#element.click()
driver.close()
