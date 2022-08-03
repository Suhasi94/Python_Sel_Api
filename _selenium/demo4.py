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
driver.get("https://www.goibibo.com/")
driver.maximize_window()
sleep(5)

driver.find_element_by_xpath("//span[text()='Departure']").click()


def select_date(month, year, day):
    _xpath = f"//div[text()='{month} {year}']/../..//p[text()='{day}']"
    for _ in range(0, 12):
        try:
            driver.find_element_by_xpath(_xpath).click()
            return True
        except NoSuchElementException:
            driver.find_element_by_xpath("//span[@aria-label='Next Month']").click()
            sleep(1)
    return False
