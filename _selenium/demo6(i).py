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

# Printing the headers
print(f"{'AAPL':>10} {'MSFT':>10} {'AA':>10} {'FB':>10}")

# Infinitely monitering the prices
while True:
    aapl_price = driver.find_element_by_xpath("//td[text()='AAPL']/..//td[3]").text
    msft_price = driver.find_element_by_xpath("//td[text()='MSFT']/..//td[3]").text
    aa_price = driver.find_element_by_xpath("//td[text()='AA']/..//td[3]").text
    fb_price = driver.find_element_by_xpath("//td[text()='FB']/..//td[3]").text

    print(f"{aapl_price:>10} {msft_price:>10} {aa_price:>10} {fb_price:>10}", end="")
    print("")
    sleep(2)