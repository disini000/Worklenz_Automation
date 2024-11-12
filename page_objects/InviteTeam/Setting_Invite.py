from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from faker import Faker

class SettingInvite:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.faker = Faker()

    def enter_data_to_login(self, wait, username, password):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def enter_data_for_invite_to_team(self, wait, email, job):
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          "/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/li[5]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          "/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/div/div[3]/ul/li[2]"))).click()
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Team Members']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add Member']"))).click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div/nz-select/nz-select-top-control/nz-select-search/input"))).send_keys(email + Keys.RETURN)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Select the job title (Optional)']"))).send_keys(job)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@type='submit']//span[text()='Add to team']"))).click()

    def invite_team_member(self):
        random_email = self.faker.email()
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")

        self.enter_data_for_invite_to_team(self.wait, random_email, "Software Tester")
        time.sleep(3)

        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        rows = t_body.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            email_cell = row.find_elements(By.TAG_NAME, "td")[2].text
            email_cell_n = email_cell.split(' (')[0]
            time.sleep(1)
            setting_email = email_cell_n.strip()
            invite_email = random_email.strip()
            if setting_email == invite_email:
                print(f"Test passed: Team member's email '{random_email}' found in the table.")
                break
        else:
            print(f"Test failed: Team member's email '{random_email}' not found in the table.")

    def invite_team_member_without_filling_jobTitle(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")

        random_email = self.faker.email()
        self.enter_data_for_invite_to_team(self.wait, random_email, "")
        time.sleep(3)

        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        rows = t_body.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            email_cell = row.find_elements(By.TAG_NAME, "td")[2].text
            email_cell_n = email_cell.split(' (')[0]
            time.sleep(1)
            setting_email = email_cell_n.strip()
            invite_email = random_email.strip()
            if setting_email == invite_email:
                print(f"Test passed: Team member's email '{random_email}' found in the table.")
                break
        else:
            print(f"Test failed: Team member's email '{random_email}' not found in the table.")


    def invite_team_member_with_invalid_email(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")

        self.enter_data_for_invite_to_team(self.wait, "hello.gmail.com", "Software Tester")

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'ant-notification-notice-description') and text()='Invalid email address']")))
            print("Test passed: invite_team_member_with_invalid_email")
        except NoSuchElementException:
            print("Test failed: invite_team_member_with_invalid_email")

    def invite_team_member_with_empty_email(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")

        self.enter_data_for_invite_to_team(self.wait, "", "Software Tester")

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='d-block' and text()='Add Member']")))
            print("Test passed: invite_team_member_with_empty_email")
        except NoSuchElementException:
            print("Test failed: invite_team_member_with_empty_email")

    def invite_team_member_with_an_email_already_added_into_team(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")

        self.enter_data_for_invite_to_team(self.wait, "hello@gmail.com", "Software Tester")

        time.sleep(3)
        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        rows = t_body.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            email_cell = row.find_elements(By.TAG_NAME, "td")[2].text
            email_cell_n = email_cell.split(' (')[0].strip()
            target_email = "hello@gmail.com"

            if email_cell_n == target_email:
                print(f"Test passed: Team member's email '{target_email}' found in the table.")
                break
        else:
            print(f"Test failed: Team member's email '{target_email}' not found in the table.")








