from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_credentials(self, username, password):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()
















# from selenium.webdriver.common.by import By
#
# class LogInPage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.email_field = "input[placeholder='Email']"
#         self.password_field = "input[placeholder='Password']"
#         self.logIn_button = "//span[normalize-space()='Log in']"
#
#     def enter_email_into_Email_field(self, username):
#         self.driver.find_element(By.CSS_SELECTOR, self.email_field).send_keys(username)
#
#     def enter_password_into_password_field(self, password):
#         self.driver.find_element(By.CSS_SELECTOR, self.password_field).send_keys(password)
#
#     def click_logIn_button(self):
#         self.driver.find_element(By.XPATH, self.logIn_button).click()