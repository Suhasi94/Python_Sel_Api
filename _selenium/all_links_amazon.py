from time import sleep

from selenium import webdriver


driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.amazon.com")
all_links = driver.find_elements_by_xpath("//a")
sleep(2)
for links in all_links:
    print(links.text)
    print(links.get_attribute("href"))