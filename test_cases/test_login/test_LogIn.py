from page_objects.login.user_login import UserLogin
from test_cases.conftest import setup
from utilities.ReadConfigurations import ReadConfig


class TestLogin:
    baseUrl = ReadConfig.get_application_url()

    def test_check_user_able_to_with_valid_data(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.check_user_able_to_with_valid_data()

    def test_check_user_unable_LogIn__with_Invalid_emailFormat(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.check_user_unable_LogIn__with_Invalid_emailFormat()

    def test_check_user_Unable_logIn_with_Invalid_Email(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.check_user_Unable_logIn_with_Invalid_Email()

    def test_check_user_Unable_to_logIn_with_Invalid_Password(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.check_user_Unable_to_logIn_with_Invalid_Password()

    def test_check_user_unableLogIn__with_Empty_field(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.check_user_unableLogIn__with_Empty_field()

    def test_SignUp_With_Google_button(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.SignUp_With_Google_button()

    def test_Check_Forgot_Password_button(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.Check_Forgot_Password_button()

    def test_remember_me_checkbox(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lg = UserLogin(self.driver)
        self.lg.remember_me_checkbox()

