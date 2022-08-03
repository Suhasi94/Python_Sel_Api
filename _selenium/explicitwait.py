

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("./chromedriver.exe")
driver.get(r"C:/Users/singh/PycharmProjects/project1new/_selenium/sir file/loading.html")
w = WebDriverWait(driver, 10)
v=visibility_of_element_located(('name', 'fname'))
w.until(v)
element = driver.find_element_by_name('fname')
element.send_keys("hello")
