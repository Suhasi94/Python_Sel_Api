import csv
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver")
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts")
driver.maximize_window()
sleep(5)

# glasses = { 'Sunglasses Aero': 139.00,
#             'ORIGINAL COLLECTION': 149.00,
#             'Custom Sunglasses': 179.00
#         }

def read_csv():
    expected_prices = { }
    with open("./sir file/smart_prices.csv") as f:
        rows = csv.reader(f)
        headers = next(rows)     # skip headers
        for row in rows:
            expected_prices[row[0]] = float(row[1])
    return expected_prices

d = read_csv()

for product, expected_price in d.items():
    _xpath = f"//span[text()='{product}']/../../..//span[@class='art-price' or @class='art-price art-price--offer']"
    temp = driver.find_element_by_xpath(_xpath).text
    actual_price = findall(r"[\d\.]", temp)
    actual_price = float("".join(actual_price))
    if actual_price == expected_price:
        print("PASS")
    else:
        print(f"FAIL: {product}: Expceted {expected_price}: actual: {actual_price}")