import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

# from wlz_automation.test_cases.BaseTest import BaseTest

class UserLogin:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_data_to_login(self, wait, username, password):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def check_user_able_to_with_valid_data(self):
        self.enter_data_to_login(self.wait,"hello23@gmail.com","heLLo12@")

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Home']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : Check_user_able_to_with_valid_data")

    def check_user_unable_LogIn__with_Invalid_emailFormat(self):
        self.enter_data_to_login(self.wait, "hello23.gmail.com", "heLLo12@")
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='alert']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : check_user_unable_LogIn__with_Invalid_emailFormat")

    def check_user_Unable_logIn_with_Invalid_Email(self):
        self.enter_data_to_login(self.wait, "heltest@gmail.com", "heLLo12@")
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Login failed!']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : check_user_Unableto_logIn_with_Invalid_Email")

    def check_user_Unable_to_logIn_with_Invalid_Password(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo112w@")

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Login failed!']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : check_user_Unable_to_logIn_with_Invalid_Password")

    def check_user_unableLogIn__with_Empty_field(self):
        self.enter_data_to_login(self.wait, "", "heLLo12@")
        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='alert']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : check_user_unableLogIn__with_Empty_field")

    def SignUp_With_Google_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Sign in with Google']"))).click()

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Create account']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : SignUp_With_Google_button")

    def Check_Forgot_Password_button(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.test_login-form-forgot[href='/auth/reset-password']"))).click()

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Reset Password']")))
        except NoSuchElementException:
            pytest.fail("Test case fail : Check_Forgot_Password ")

    def remember_me_checkbox(self):
        remember_me_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[span/span[text()='Remember me']]")))
        first_class_name = remember_me_box.get_attribute("class")

        remember_me_box.click()
        changed_class_name = remember_me_box.get_attribute("class")

        if first_class_name != changed_class_name:
            print("RememberMe Checkbox has checked.")
        else:
            pytest.fail("Test case failed: 'Remember me' checkbox did not check after clicking.")
