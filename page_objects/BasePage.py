
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def type_into_element(self,locator_name,locator_value,text,):
        element = self.get_element(locator_name,locator_value)
        # element.click()
        # element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.endswith("_id"):
            element = self.wait.until(EC.visibility_of_element_located((By.ID, locator_value)))
        elif locator_name.endswith("_name"):
            element = self.wait.until(EC.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_name.endswith("_class_name"):
            element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_name.endswith("_link_text"):
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_name.endswith("_xpath"):
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator_value)))
        elif locator_name.endswith("_css"):
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,locator_value)))
        elif locator_name.endswith("_tag_name"):
            element = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, locator_value)))
        return element