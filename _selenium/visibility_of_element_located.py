from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(r"C:\Users\singh\PycharmProjects\project1new\_selenium\sir file\progressbar.html")
driver.find_element_by_xpath("//button[text()='Click Me']").click()
driver.maximize_window()
w = WebDriverWait(driver,20)
v = visibility_of_element_located(('text', '100%'))
w.until(v)
print("Done")







