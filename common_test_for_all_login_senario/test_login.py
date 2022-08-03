
from common_test_for_all_login_senario.loginpage import LoginPage
from common_test_for_all_login_senario.homepage import HomePage
from pytest_testNG.conftest import setup
def test_login(setup):
    hp = HomePage(setup)
    hp.click_login()
    lp = LoginPage(setup)
    lp.enter_email("hello.world@company.com")
    lp.enter_password("Password123")
    lp.click_login()