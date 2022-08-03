from registration_file_pending_incommon_test_with_assert.homepage import HomePage
from registration_file_pending_incommon_test_with_assert.registrationpage import RegistrationPage
from pytest_testNG.conftest import setup
def test_registration(setup):
    hp = HomePage(setup)
    # Click on Register Link
    hp.home_click_register()
    # Click Either Male or Female radio button
    rp = RegistrationPage(setup)
    rp.reg_select_male()
    # Enter Fname
    rp.reg_enter_fname("steve")
    # Enter Lname
    rp.reg_enter_lname("jobs")
    # Enter Email
    rp.reg_enter_email("steve.jobs@company.com")
    # Enter Password
    rp.reg_enter_password("Password123")
    # Enter Confirm Password
    rp.reg_enter_confirm_password("Password123")
    # Click Register
    rp.reg_click_register()
