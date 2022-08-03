import csv
from selenium import webdriver
from re import findall
d = {}

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")

with open(r"sir file/smart_prices.csv") as file:
    rows = csv.reader(file)
    header = next(rows)
    for row in rows:
        d[row[0]] = row[1]
for name, price in d.items():

    actual_price = driver.find_element_by_xpath(f"//span[text()='{name}']/../../..//span[@class='art-price' or @class = 'art-price art-price--offer']").text
    actual = findall(r"[\d\.]", actual_price)
    actual = "".join(actual)
    if float(price) == float(actual):
        print(f"{name} is passed ")
    else:
        print(f"{name} is failed ")






