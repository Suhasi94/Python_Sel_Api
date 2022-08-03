from selenium.common.exceptions import NoSuchElementException
from time import sleep
from common_test_for_all_login_senario.excel_lib import read_locators
from inter_connected_all.selenium_wrapper import SeleniumWrapper


class HomePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        
    locators = read_locators("homepage")
    def click_login(self):
        element = HomePage.locators['lnk_login']
        self.click_element(element)
    
    def home_click_register(self):
        element = HomePage.locators['lnk_register']
        self.click_element(element)

    def is_user_logged_in(self, email):
        _xpath = f"//a[text()='{email}']"
        for _ in range(10):
            try:
                return self.driver.find_element("xpath", _xpath).is_displayed()
            except NoSuchElementException:
                print("User is not logged in yet.. trying after one second")
                sleep(1)
                continue
        return False