from time import sleep
from selenium.webdriver import Chrome
from pytest import fixture
from inter_connected_all.config import Config

@fixture(scope="function")


def setup():
    print("Running Setup")
    #from inter_connected_all.config import Config
    driver = Chrome(Config.DRIVER_PATH)
    print(driver)
    driver.get(Config.URL)
    driver.maximize_window()
    sleep(3)
    yield driver
    print("Closing Browser")
    driver.close()

@fixture
def hello():
    print("hello world")
    yield "hi there"
    print("Bye world")
