
from selenium.webdriver.common.by import By
from inter_connected_all.selenium_wrapper import SeleniumWrapper

def test_registration(setup):
    s = SeleniumWrapper(setup)
    s.click_element((By.LINK_TEXT, "Register"))
    s.click_element((By.ID, "gender-male"))
    s.enter_text((By.NAME, "FirstName"), value="hello")
    s.enter_text((By.XPATH, "//input[@name='LastName']"), value="world")
    s.enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")
    s.enter_text((By.ID, "Password"), value="Password123")
    s.enter_text((By.ID, "ConfirmPassword"), value="Password123")
    s.click_element((By.ID, "register-button"))