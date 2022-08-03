from select import select
from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://services.smartbear.com/samples/TestComplete14/smartstore/spiegel-bestseller")
driver.maximize_window()
sleep(5)
var=driver.find_element_by_xpath("(//a[@class='facet-group-header facet-toggle collapsed'])[1]").click()
all_links = driver.find_elements_by_xpath("//div[@class='facet-body-inner']/div/label/span[@class='facet-control-ui']")
sleep(2)
i=0
while i <= len(all_links):
    i+=1
    try:



