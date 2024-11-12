import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class UserDependency:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def enter_data_to_login(self,wait, username,password):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def open_task_form_from_a_task(self,wait,row_index):
        wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Projects']"))).click()
        time.sleep(1)
        t_body = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        row_1 = t_body_wait.until(EC.visibility_of_all_elements_located((By.XPATH, "tr")))[1]
        rows_wait = WebDriverWait(row_1, 10)
        rows_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "td")))[0].click()
        task_row_1 = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[row_index]
        task_row_1_wait = WebDriverWait(task_row_1, 10)
        task_row_1_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "task-name-text"))).click()
        task_inner = self.driver.find_element(By.CLASS_NAME, "inner-task-name-container")
        task_open = task_inner.find_element(By.TAG_NAME, "button")
        task_open.click()

    def click_Add_dependency(self,wait):
        add_dependency = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='+ Add new dependency']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_dependency)
        add_dependency.click()

    def close_task_form(self,wait):
        close_form = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[1]/div[1]/button/span")))
        close_form.click()

    def change_status_to_done_from_TO_DO_Task(self,wait):
        task_row_1 = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[0]
        task_row_1_wait = WebDriverWait(task_row_1, 10)
        task_row_1_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-list-status")))
        status_change = self.driver.find_element(By.XPATH,
                                                 "//nz-select-item[@class='ant-select-selection-item ng-star-inserted' and @title='To do']")
        status_change.click()
        status_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")))
        status = status_dropdown.find_elements(By.TAG_NAME, 'nz-option-item')
        status[2].click()
        time.sleep(5)

    def add_dependency_to_the_task_In_ToDo(self):
        is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait, 0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        task_name = "Test create new project task"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(task_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()

        time.sleep(4)
        t_body = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-task-view-dependencies//tbody")))
        dependency_lists = t_body.find_elements(By.TAG_NAME, "tr")
        for dependency_list in dependency_lists:
            dependency_names = dependency_list.find_elements(By.TAG_NAME, "td")[0].text
            dependency_names_new = dependency_names.replace("WA-4", "").strip()
            time.sleep(1)

            if dependency_names_new in task_name:
                print(f"Test passed: New Dependency name '{task_name}' found in the table.")
                is_dependency = True
                break

        if is_dependency:
            pass
        else:
            pytest.fail(f"Test failed: New Dependency name '{task_name}' not found in the table.")


    def dependency_symbol_appears(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        task_name = "writting test plan"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(task_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='writting test plan']"))).click()

        time.sleep(2)
        self.close_task_form(self.wait)

        refresh = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[nz-icon][nztype='sync']")))
        refresh.click()

        time.sleep(2)
        task_row_1 = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[0]
        task_row_1_wait = WebDriverWait(task_row_1, 10)
        task_row_1_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inner-task-name-container")))
        icon_inner = self.driver.find_element(By.CLASS_NAME, "inner-icon-cont")
        dependency_icon =  icon_inner.find_element(By.CSS_SELECTOR, "span[nz-icon][nztype='minus-circle']")
        if dependency_icon.is_displayed():
            print("Dependency icon is displayed.")
        else:
            print("Dependency icon is not displayed.")


    def add_multiple_dependency_to_the_task(self):
        is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name = "edbuh"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='edbuh']"))).click()

        time.sleep(4)
        t_body = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-task-view-dependencies//tbody")))
        dependency_lists = t_body.find_elements(By.TAG_NAME, "tr")
        for dependency_list in dependency_lists:
            dependency_names = dependency_list.find_elements(By.TAG_NAME, "td")[0].text
            dependency_names_new = dependency_names.replace("WA-12", "").strip()
            time.sleep(1)

            if dependency_names_new in dependency_task_name:
                print(f"Test passed: New Dependency name '{dependency_task_name}' found in the table.")
                is_dependency = True
                break

        if is_dependency:
            pass
        else:
            pytest.fail(f"Test failed: New Dependency name '{dependency_task_name}' not found in the table.")


    def delete_Dependency_from_Task(self):
        #is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name = "testing hello"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='testing hello']"))).click()

        time.sleep(5)

        delete_button = self.driver.find_element(By.XPATH, "//nz-table//tr[1]//td[3]//button//span[contains(@class, 'anticon-delete')]")
        delete_button.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Yes']"))).click()

        time.sleep(1)

        t_body = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-task-view-dependencies//tbody")))
        dependency_lists = t_body.find_elements(By.TAG_NAME, "tr")

        is_deleted = False
        for dependency_list in dependency_lists:
            dependency_names = dependency_list.find_elements(By.TAG_NAME, "td")[0].text
            dependency_names_new = dependency_names.replace("WA-6", "").strip()

            if dependency_task_name == dependency_names_new:
                is_deleted = False
                print(f"Task '{dependency_task_name}' still exists in the table.")
                break
            else:
                is_deleted = True

        if is_deleted:
            print(f"Test passed: Dependency '{dependency_task_name}' has been successfully deleted.")
        else:
            pytest.fail(f"Test failed: Dependency '{dependency_task_name}' still exists in the table")


    def change_Status_After_Deleting_Dependency(self):
        is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        # use
        task_view_name = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-view-name")))
        task_view_name_wait = WebDriverWait(task_view_name, 10)
        task_name = task_view_name_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p"))).text

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        task_dependency_name = "testing hello"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(task_dependency_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='testing hello']"))).click()

        time.sleep(5)
        delete_button = self.driver.find_element(By.XPATH, "//nz-table//tr[1]//td[3]//button//span[contains(@class, 'anticon-delete')]")
        delete_button.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Yes']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)

        done_table = self.driver.find_element(By.ID, "6ef8284c-54ac-41bd-b8e2-d7d7ac7d864f")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", done_table)
        task_rows = done_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        # array = []
        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text
            a = task_name
            if task_name.strip() == task_name_text_after.strip():
                print(f"Test passed: task name '{task_name}' found in the Done list.")
                is_dependency = True
                break

        if is_dependency:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the Done list.")

    def change_task_TO_Done_with_Done_Dependency(self):
        is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)
        #use
        task_view_name = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-view-name")))
        task_view_name_wait = WebDriverWait(task_view_name, 10)
        task_name = task_view_name_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p"))).text

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        task_dependency_name = "Test SignIn"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(task_dependency_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test SignIn']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)

        done_table = self.driver.find_element(By.ID, "6ef8284c-54ac-41bd-b8e2-d7d7ac7d864f")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", done_table)
        task_rows = done_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text
            a = task_name
            if task_name.strip() == task_name_text_after.strip():
                print(f"Test passed: task name '{task_name}' found in the list.")
                is_dependency = True
                break

        if is_dependency:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the list.")


    def change_task_to_Done_when_all_dependancies_are_Done(self):
        is_dependency = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)
        # use
        task_view_name = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-view-name")))
        task_view_name_wait = WebDriverWait(task_view_name, 10)
        task_name = task_view_name_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "p"))).text

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name1 = "asshd"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='asshd']"))).click()

        add_dependency = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='+ Add new dependency']")))
        add_dependency.click()
        dependency_task_name2 = "edbuh"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='edbuh']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)

        done_table = self.driver.find_element(By.ID, "6ef8284c-54ac-41bd-b8e2-d7d7ac7d864f")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", done_table)
        task_rows = done_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text
            a = task_name
            if task_name.strip() == task_name_text_after.strip():
                print(f"Test passed: task name '{task_name}' found in the list.")
                is_dependency = True
                break

        if is_dependency:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the list.")


    def change_Task_as_Done_when_Dependency_is_in_ToDoing(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)
        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name = "Test create new project"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Incomplete Dependencies!']")))
            print("Test case pass : unable_to_change_task_to_Done_with_Not_Done_Dependency")
        except NoSuchElementException:
            pytest.fail("Test case fail : unable_to_change_task_to_Done_with_Not_Done_Dependency")


    def change_task_to_Done_when_one_of_dependancy_are_not_Done(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name1 = "asshd"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='asshd']"))).click()

        add_dependency = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='+ Add new dependency']")))
        add_dependency.click()
        dependency_task_name2 = "testing hello"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='testing hello']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Incomplete Dependencies!']")))
            print("Test case pass : Change_task_to_Done_when_one_of_dependancy_are_not_Done")
        except NoSuchElementException:
            pytest.fail("Test case fail : Change_task_to_Done_when_one_of_dependancy_are_not_Done")


    def add_dependency_to_the_Subtask(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Projects']"))).click()
        time.sleep(1)
        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        row_1 = t_body_wait.until(EC.visibility_of_all_elements_located((By.XPATH, "tr")))[1]
        rows_wait = WebDriverWait(row_1, 10)
        rows_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME,"td")))[0].click()
        task_row_1 = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[0]
        subtask_row = task_row_1.find_element(By.XPATH, "//span[@class='anticon anticon-double-right' and @nz-icon='']")
        subtask_row.click()
        time.sleep(5)
        subtask_row_wait = WebDriverWait(subtask_row, 15)
        subtask_row_wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='task-name-text ng-star-inserted' and contains(text(), 'write test cases')]"))).click()
        time.sleep(5)
        task_inner = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inner-task-name-container")))
        task_open_wait = WebDriverWait(task_inner, 10)
        task_open_wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()

        time.sleep(2)
        add_dependency = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='+ Add new dependency']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_dependency)
        add_dependency.click()

        dependency_task_name = "Test create new project"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()

        self.close_task_form(self.wait)

        time.sleep(2)
        self.change_status_to_done_from_TO_DO_Task(self.wait)


    def add_same_dependency_to_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)

        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name = "Test create new project"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()

        add_dependency = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='+ Add new dependency']")))
        add_dependency.click()
        dependency_task_name = "Test create new project"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Task dependency already exists.']")))
            print("Test case pass : Add_same_dependency_to_the_task")
        except NoSuchElementException:
            pytest.fail("Test case fail : Add_same_dependency_to_the_task")


    def test_Add_Non_existent_task_as_dependencies(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_task_form_from_a_task(self.wait,0)
        time.sleep(2)
        self.click_Add_dependency(self.wait)

        dependency_task_name = "Test filter function"
        task_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-12']/div/div[2]/div/div/div[2]/nz-skeleton/nz-tabset/div/div/div[1]/worklenz-task-view-info/nz-collapse/nz-collapse-panel[4]/div[2]/div/worklenz-task-view-dependencies/div[2]/div[1]/nz-select/nz-select-top-control/nz-select-search/input")))
        task_input.send_keys(dependency_task_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-item[@title='Test create new project']"))).click()
