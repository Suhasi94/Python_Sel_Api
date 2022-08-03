# 1. Go to Homepage https://automationtest.mybigcommerce.com/
# 2. Click and open Kitchen category
# 3. From the result list hover over the product image of [Sample] 1 L Le Parfait Jar
#  and click on quick view button
# 4. On the pop up page opened Select  2nd entries on the available product options and product quantity as 3
# 5. From the product description marked down below, print the description in Console log
# 6. Click add to Cart -> Proceeed to checkout
# 7. place the order as guest.
# 	Parameters:
# 	email : test.webkul@maildrop.cc
# 	Address: H33, Sector 63, Noida, UP, 201301
# 	Shipping: Flat rate
# 	Payment: Cash On delivery

from time import sleep
from selenium import webdriver
driver= webdriver.Chrome("./chromedriver.exe")
driver.get("https://automationtest.mybigcommerce.com/")
driver.find_element_by_xpath("(//li[@class='navPages-item'])[4]").click()
driver.find_element_by_xpath("(//button[text()='Quick view'])[3]").click()
sleep(2)
driver.find_element_by_xpath("//span[@title='Silver']").click()
driver.find_element_by_xpath("(//label[@class='form-option'])").click()
driver.find_element_by_xpath("//input[@value='Add to Cart']").click()
sleep(2)
driver.find_element_by_xpath("(//a[@class='button button--primary'])[1]").click()
sleep(3)
driver.find_element_by_xpath("(//input[@name='email'])[1]").send_keys("test.webkul@maildrop.cc")
sleep(1)
driver.find_element_by_xpath("//button[text()='Continue as guest']").click()