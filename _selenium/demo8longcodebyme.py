from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("./chromedriver.exe")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()

class _visibility_of_element_located(visibility_of_element_located):
    def __init__(self,locator):
        super().__init__(locator)

    def __call__(self, driver):
        result=super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False


def _wait(func):
    def wrapper(*args, **kwargs):
        locator = args[0]
        w=WebDriverWait(driver,20)
        v=_visibility_of_element_located(locator)
        w.until(v,message="progress bar was not loaded even after 20 seconds ")
        return func(*args,**kwargs)
    return wrapper

@_wait
def click_element(locator):
    driver.find_element(*locator).click()

@_wait
def enter_text(locator,*,value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)

@_wait
def select_item(locator,*,item):
    element = driver.find_element(*locator)
    s = Select(element)
    if isinstance(item,str):
        s.select_by_visible_text(item)
    elif isinstance(item,int):
        s.select_by_index(item)
    else:
        raise Exception

click_element((By.LINK_TEXT, "Register"))
click_element((By.ID, "gender-male"))
enter_text((By.NAME, "FirstName"), value="hello")
enter_text((By.XPATH, "//input[@name='LastName']"), value="world")
enter_text((By.CSS_SELECTOR, "input[name='Email']"), value="hello.world@company.com")
enter_text((By.ID, "Password"), value="Password123")
enter_text((By.ID, "ConfirmPassword"), value="Password123")
click_element((By.ID, "register-button"))
driver.close()


