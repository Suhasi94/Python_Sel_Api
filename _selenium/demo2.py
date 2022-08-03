import csv
from re import findall
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome("./chromedriver")
driver.get("https://www.monsterindia.com/")
driver.maximize_window()
sleep(5)

# Finding all the links that are present on the left navigation pane
# links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
# headers = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//h3")
# links = driver.find_elements_by_xpath("//div[@class='footer-main-wrapper']//a")

driver.find_element_by_id("SE_home_autocomplete").send_keys("HTML")
# sleep(2)
driver.find_element_by_xpath("//input[@value='Search']").submit()
sleep(5)

titles = driver.find_elements_by_xpath("//div[@class='job-tittle']/h3/a")
sleep(2)
for title in titles:
    print(title.text)
    sleep(1)

    # for header in headers:
    #     print(header.text)
    #     sleep(1)

    # for link in links:
    #     print(link.text)
    #     sleep(1)