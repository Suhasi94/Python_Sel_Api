from common_test_for_all_login_senario.excel_lib import read_locators
from inter_connected_all.selenium_wrapper import SeleniumWrapper


class HomePage(SeleniumWrapper):
    def __init__(self, driver):
        super().__init__(driver)
        
    locators = read_locators("homepage")
    def home_click_login(self):
        element = HomePage.locators['lnk_login']
        self.click_element(element)
    
    def home_click_register(self):
        element = HomePage.locators['lnk_register']
        self.click_element(element)