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

driver.get("http://demowebshop.tricentis.com/books")

driver.maximize_window()
sleep(3)

lst_box = driver.find_element_by_name("products-orderby")
s = Select(lst_box)
s.select_by_visible_text("Name: A to Z")
sleep(5)

lst_box = driver.find_element_by_id("products-orderby")
s = Select(lst_box)
s.select_by_visible_text("Price: Low to High")


lnk_register = driver.find_elements_by_link_text("Register")
print(lnk_register)
lnk_register[0].click()
sleep(5)

# lnk_register = driver.find_element_by_link_text("Register")
# print(lnk_register)
# lnk_register.click()
# sleep(5)









