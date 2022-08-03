from gettext import find

from selenium import webdriver
from time import sleep

#WebDriver driver = new ChromeDriver();

driver = webdriver.Chrome('./chromedriver')

#driver.get("file:///C:/Users/singh/OneDrive/Desktop/html%20practice/handilingselinium.html");

driver.get("https://www.google.com")
sleep(1)
driver.maximize_window()
sleep(2)
element=driver.find_element_by_css_selector("input[name='q']")
key = "iphone"
element.send_keys(key)
driver.implicitly_wait(10)
all_suggestion = driver.find_elements_by_xpath("//ul[@role='listbox']/li/div/div[2]")

#all_suggestion = driver.find_elements_by_xpath('//li[@role="presentation"]//div[@role="option"]')


for suggestion in all_suggestion:
    print(suggestion.text)


#driver.quit()
