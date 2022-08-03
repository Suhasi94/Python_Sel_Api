from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.google.com")
driver.find_element("xpath","//input[@class='gLFyf gsfi']").send_keys("selenium")
