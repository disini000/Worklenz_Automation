from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_invite(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Invite']"))).click()

    def invite_team_member(self, email, job=""):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='cdk-overlay-0']/div/div[2]/div/div/div[2]/nz-spin/div/form/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"))
        ).send_keys(email + Keys.RETURN)
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Select the job title (Optional)']"))
        ).send_keys(job)

    def submit_invite(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']//span[text()='Add to team']"))).click()

    # def get_team_members(self):
    #     self.driver.get("https://uat.app.worklenz.com/worklenz/settings/team-members")
    #     t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
    #     return t_body.find_elements(By.TAG_NAME, "tr")
