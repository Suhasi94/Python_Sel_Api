import csv
from selenium.common.exceptions import NoSuchElementException
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("./chromedriver")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//a[@title='Follow us on Twitter']").click()
sleep(5)

handles = driver.window_handles
driver.switch_to.window(handles[1])
sleep(3)

driver.find_element_by_xpath("//input[@placeholder='Search Twitter']").send_keys("hello")
sleep(2)

driver.switch_to.window(handles[0])
sleep(2)
driver.switch_to.window(handles[1])
sleep(2)
driver.close()
driver.switch_to.window(handles[0])
sleep(1)

text = driver.find_element_by_xpath("//a[text()='Register with us']").click()

sleep(2)


for handle in handles:
    print(handle)


driver.find_element_by_id("delete").click()
sleep(1)

driver.switch_to.alert.accept()
sleep(1)

driver.find_element_by_id("delete").click()
sleep(1)

print(driver.switch_to.alert.text)

driver.switch_to.alert.dismiss()
