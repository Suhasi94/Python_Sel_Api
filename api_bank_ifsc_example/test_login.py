from api_bank_ifsc_example.loginpage import LoginPage
from api_bank_ifsc_example.homepage import HomePage
from pytest import mark
from common_test_for_all_login_senario.excel_lib import read_headers, read_data

headers = read_headers("smoke", "test_login_positive")
data = read_data("smoke", "test_login_positive")

@mark.parametrize(headers, data)
def test_login_positive(setup, email, password):
    hp = HomePage(setup)
    hp.home_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    assert lp.is_user_logged_in(email) == True
#
headers = read_headers("smoke", "test_login_negative")
data = read_data("smoke", "test_login_negative")

@mark.parametrize(headers, data)
def test_login_negative(setup, email, password, error_message):
    hp = HomePage(setup)
    hp.home_click_login()
    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    assert lp.is_auth_error_displayed(error_message) == True
