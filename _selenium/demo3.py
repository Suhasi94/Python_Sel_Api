import csv
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement

driver = Chrome("./chromedriver.exe")
driver.get(r"C:\Users\singh\PycharmProjects\project1new\_selenium\sir file\loading.html")
driver.maximize_window()

# 1. Check if the element is loaded in the DOM
# 2. Check if the element is visible on the webpage.
# 3. Check if the element is enabled or not?

class _visibility_of_element_located(visibility_of_element_located):


    def __init__(self, locator):



        super().__init__(locator)   # initlising parent class constructor


    # over-riding __call__ method of parent class
    def __call__(self, driver):
        print("Calling __call__ method of Child Class")
        result = super().__call__(driver)
        if isinstance(result, WebElement):
            # Extra functionality that you are adding in child class
            # checking for enablement of the element
            return result.is_enabled()
        else:
            return False

w = WebDriverWait(driver, 20)


v = _visibility_of_element_located(("name", "fname"))
w.until(v)
driver.find_element_by_name("fname").send_keys("hello")