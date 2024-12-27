import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from faker import Faker

class ProjectInside:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.faker = Faker()

    def enter_data_to_login(self, wait, username, password):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def open_a_project(self, wait):
        wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Projects']"))).click()
        time.sleep(1)
        t_body = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        row_1 = t_body_wait.until(EC.visibility_of_all_elements_located((By.XPATH, "tr")))[1]
        rows_wait = WebDriverWait(row_1, 10)
        rows_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "td")))[0].click()

    #function for Change category test case
    def get_background_color(self):
        element = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[@class='ant-btn collapse btn border-0 active']")))

        # Extract the background color from the style attribute
        style = element.get_attribute("style")
        background_color = None
        if "background-color" in style:
            background_color = style.split("background-color:")[-1].split(";")[0].strip()
            print(background_color)
        return background_color

    def Verify_UI_Elements_in_Tasklist(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        time.sleep(5)

        try:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[nz-icon][nztype='search']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Sort']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Priority']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Labels']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Members']"))).click()

            #GropBy
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='ant-btn ant-dropdown-trigger ms-1 button-mobile']//span[contains(text(),'Status')]"))).click()

            #show archived
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Show archived']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Show archived']"))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Show fields']"))).click()

            #show fields
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='drag-handle ng-star-inserted']")))

            #Bulb action menu and Context menu
            checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@nz-checkbox]//input[@type='checkbox'])[2]")))
            checkbox.click()
            ActionChains(self.driver).context_click(checkbox).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='bulk-actions open']")))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'ant-dropdown-menu')]")))

            #Timelog details
            self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//span[@class='ng-star-inserted' and text()='0m 0s'])[1]"))).click()
            print("Test case Pass: Verify UI Elements in Tasklist.")

        except TimeoutException:
            pytest.fail("Test case fail : Verify UI Elements in Tasklist.")

    def Verify_Tooltips_in_Tasklist(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        time.sleep(5)

        try:
            groupBy_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[@class='ant-btn ant-dropdown-trigger ms-1 button-mobile']//span[contains(text(),'Status')]")))
            ActionChains(self.driver).move_to_element(groupBy_element).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ant-tooltip-inner') and text()='Status']")))

            taskName_element = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                "(//div[@class='inner-task-name-container']//div[contains(@class, 'task-name-text')])[1]")))
            ActionChains(self.driver).move_to_element(taskName_element).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Open'])[1]")))

            key_element = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                             "(//nz-tag[@class='ant-tag m-0'])[1]")))
            ActionChains(self.driver).move_to_element(key_element).perform()

            label_element2 = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                "(//nz-tag[@class='ant-tag text-dark task-list-label ant-tag-has-color ng-star-inserted'])[1]")))
            ActionChains(self.driver).move_to_element(label_element2).perform()

            progress_element = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                             "(//nz-progress[@class='ng-star-inserted'])[1]")))
            ActionChains(self.driver).move_to_element(progress_element).perform()

            member_element2 = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                             "(//nz-avatar[@class='ant-avatar ant-avatar-circle ant-avatar-image ng-star-inserted'])[2]")))
            ActionChains(self.driver).move_to_element(member_element2).perform()

            #Status description tooltips
            self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[starts-with(@class, 'ant-btn ant-dropdown-trigger p-0')])[1]"))).click()
            change_category = self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@nz-submenu]")))
            change_category.click()
            status_element1 = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                              "//li//nz-badge//span[contains(text(), 'Doing')]")))
            status_element2 = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                              "//li//nz-badge//span[contains(text(), 'Done')]")))
            ActionChains(self.driver).move_to_element(status_element1).perform()
            ActionChains(self.driver).move_to_element(status_element2).perform()

            print("Test case Pass: Verify Tooltips in Tasklist.")

        except NoSuchElementException:
            pytest.fail("Test case fail : Verify Tooltips in Tasklist.")

    def verify_task_creation_via_Create_task(self):
        task_list_tasks = []
        is_task = False
        status_name = self.faker.sentence()
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Task']"))).click()

        task_view_name = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-view-name")))
        task_view_name.click()
        task_input = WebDriverWait(task_view_name, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        task_input.click()
        task_input.send_keys(Keys.CONTROL,"a", Keys.BACKSPACE)
        task_input.send_keys(status_name + Keys.ENTER)
        time.sleep(5)

        toDo_table = self.driver.find_element(By.XPATH,
                                              "(//div[@class='cdk-drop-list container px-0 table-container table-1'])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", toDo_table)
        task_rows = toDo_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")

        for task_row in task_rows:
            task_name_text = task_row.find_element(By.CLASS_NAME, "task-name-text").text.strip()
            task_list_tasks.append(task_name_text)

            if status_name in task_list_tasks:
                print(f"Test passed: task name found in the ToDo list.")
                is_task = True
                break

        if is_task:
            pass
        else:
            pytest.fail(f"Test failed: task name not found in the ToDo list.")

    def verify_task_creation_Via_Import_task(self):
        import_tasks = []
        task_list_tasks = []
        is_task = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@nz-icon][@nztype='down'])[1]"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='ant-dropdown-menu-item']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//nz-select[@name='template']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//nz-option-item)[2]"))).click()

        parent_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-list-items.ng-star-inserted")))
        list_items = WebDriverWait(parent_element, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ant-list-item")))

        for item in list_items:
            task_name_ = item.text.strip()
            task_name =task_name_.split('\nRemove')[0]
            import_tasks.append(task_name)

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Import']"))).click()
        time.sleep(5)

        toDo_table = self.driver.find_element(By.XPATH, "(//div[@class='cdk-drop-list container px-0 table-container table-1'])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", toDo_table)
        task_rows = toDo_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")

        for task_row in task_rows:
            task_name_text = task_row.find_element(By.CLASS_NAME, "task-name-text").text.strip()
            task_list_tasks.append(task_name_text)

        A = task_rows
        b = import_tasks
        for import_task in import_tasks:

            if import_task not in task_list_tasks:
                pytest.fail(f"Test failed: New imported task not found in the table.")
                break

    def verify_rename_the_status(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[starts-with(@class, 'ant-btn ant-dropdown-trigger p-0')])[1]"))).click()
        rename_status = self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='ant-dropdown-menu-item']")))
        rename_status.click()

        status_name = self.faker.word()
        input_xpath = "//input[@id='group-name-70672fd4-4d1c-4c0e-805f-763b0337a023']"
        status = self.wait.until(EC.visibility_of_element_located((By.XPATH, input_xpath)))
        status.click()
        status.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        status.send_keys(status_name + Keys.ENTER)
        time.sleep(5)

        # status_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//button[@class='ant-btn collapse btn border-0 active'])[1]")))
        # task_list_name_element = WebDriverWait(status_button, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//worklenz-task-list-group-settings//button[1]/span[2]")))
        # attribute_value = task_list_name_element.get_attribute("text")
        # print(f"Attribute value: {attribute_value}")


        # task_list_name = WebDriverWait(status_button, 10).until(EC.presence_of_element_located((By.XPATH, "//worklenz-task-list-group-settings//button[1]/span[2]")))
        # Updated_name_ = task_list_name.text.strip()
        # print(Updated_name_)
        #updated_name =  Updated_name_.split('\nRemove')[0]


    def verify_Change_category(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)

        first_color = self.get_background_color()

        self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//button[starts-with(@class, 'ant-btn ant-dropdown-trigger p-0')])[1]"))).click()

        # Select "Change Category" option
        change_category = self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[@nz-submenu]")))
        change_category.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//li//nz-badge//span[contains(text(), 'Done')]"))).click()
        time.sleep(5)
        final_color = self.get_background_color()

        if first_color != final_color:
            print("Test case Passed: verify_Change_category.")
        else:
            pytest.fail("Test case failed: 'verify_Change_category.")

    def verify_Add_a_task(self):
        task_name = self.faker.name()
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[span[text()=' Add Task']])[1]"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type your task and hit enter']"))).send_keys(task_name + Keys.ENTER)
        time.sleep(5)

        is_task = False
        toDo_table = self.driver.find_element(By.XPATH,
                                              "(//div[@class='cdk-drop-list container px-0 table-container table-1'])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", toDo_table)
        task_rows = toDo_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")

        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text.strip()
            print(f"Task in ToDo list: {task_name_text_after}")

            if task_name in task_name_text_after:
                print(f"Test passed: task name '{task_name}' found in the ToDo list.")
                is_task = True
                break

        if is_task:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the ToDo list.")

    def verify_Add_a_subtask(self):
        task_name = self.faker.name()
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='flex-row task-arrow']//span[contains(@class, 'anticon-right')])[1]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[span[text()=' Add sub-task']])[1]"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type your task and hit enter']"))).send_keys(task_name + Keys.ENTER)
        time.sleep(5)

        is_task = False
        subtask_lists = self.driver.find_element(By.XPATH, "(//div[@class='ng-star-inserted'])[1]")
        task_rows = subtask_lists.find_elements(By.TAG_NAME, "worklenz-task-list-row")

        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text.strip()
            print(f"Task in ToDo list: {task_name_text_after}")

            if task_name in task_name_text_after:
                print(f"Test passed: task name '{task_name}' found in the ToDo list.")
                is_task = True
                break

        if is_task:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the ToDo list.")

    def verify_edit_the_task(self):
        task_name = self.faker.word()
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        task_name_click = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                        "(//div[@class='inner-task-name-container']//div[contains(@class, 'task-name-text')])[1]")))
        task_name_click.click()
        # edit_task_name = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        edit_task_name = WebDriverWait(task_name_click, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        edit_task_name.click()
        edit_task_name.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
        edit_task_name.send_keys(task_name + Keys.ENTER)


    def verify_Assign_members_to_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)

        # Get the initial avatar count before assigning the member
        members_column = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "worklenz-task-list-members")))
        members_column_wait = WebDriverWait(members_column, 10)
        avatar_group = members_column_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-avatars")))
        avatars_before = len(WebDriverWait(avatar_group, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'nz-avatar'))))

        print(f"Before assigning member: {avatars_before}")

        # Assign member to the task
        self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                        "(//nz-avatar[contains(@class, 'add-button')])[1]"))).click()
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//li[@nz-checkbox and @nz-menu-item])[3]"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='OK']"))).click()
        time.sleep(3)

        avatars_after = len(avatar_group.find_elements(By.TAG_NAME, 'nz-avatar'))
        print(f"After assigning member: {avatars_after}")

        if avatars_after > avatars_before:
            print("Member successfully assigned!")
        else:
            print("No change in avatar count.")

    def verify_Add_label_to_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                        "(//nz-tag[@class='ant-tag text-dark avatar-dashed empty-label task-list-label'])[1]"))).click()
        label_option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//li[@nz-checkbox and @nz-menu-item])[3]")))
        label_text = label_option.text
        print(f"Selected label: {label_text}")
        label_option.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='OK']"))).click()
        time.sleep(3)

        is_label = False
        label_column = self.driver.find_element(By.TAG_NAME, "worklenz-task-list-labels")
        label_tags = label_column.find_elements(By.TAG_NAME, "nz-tag")

        for  label_tag in  label_tags:
            label_name_text =  label_tag.text.strip()
            #print(f"Task in ToDo list: {label_name_text}")

            if label_text in label_name_text:
                print(f"Test passed: label_text found ")
                is_label = True
                break

        if is_label:
            pass
        else:
            pytest.fail(f"Test failed: label_text not found")

    def verify_Change_status_of_the_task(self):
        is_task = False
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)

        task_row_1 = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[0]
        task_row_1_wait = WebDriverWait(task_row_1, 10)
        task_name = task_row_1_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "task-name-text"))).text

        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//worklenz-task-list-row//worklenz-task-list-status//nz-select)[1]"))).click()
        status_option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-option-container//nz-option-item[3]")))
        status_option.click()
        time.sleep(5)

        done_table = self.driver.find_element(By.ID, "6ef8284c-54ac-41bd-b8e2-d7d7ac7d864f")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", done_table)
        task_rows = done_table.find_elements(By.TAG_NAME, "worklenz-task-list-row")

        for task_row in task_rows:
            task_name_text_after = task_row.find_element(By.CLASS_NAME, "task-name-text").text
            a = task_name
            if task_name.strip() == task_name_text_after.strip():
                print(f"Test passed: task name '{task_name}' found in the Done list.")
                is_task = True
                break

        if is_task:
            pass
        else:
            pytest.fail(f"Test failed: task name '{task_name}' not found in the Done list.")

    def verify_Change_phase_of_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//worklenz-task-list-row//worklenz-task-list-phase//nz-select)[1]"))).click()
        phase_option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//cdk-virtual-scroll-viewport/div/nz-option-item)[3]")))
        phase_text = phase_option.text
        #print(f"Selected phase: {phase_text}")
        phase_option.click()
        time.sleep(5)

        Updated_phase = self.wait.until(EC.visibility_of_element_located
                                        ((By.XPATH, "//worklenz-task-list-row[1]//worklenz-task-list-phase//nz-select//nz-select-top-control//nz-select-item"))).text
        #print(Updated_phase)

        if phase_text in Updated_phase:
            print("Test passed:")

        else:
            print("Test failed:")

    def verify_Change_priority_of_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        status = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//worklenz-task-list-row//worklenz-task-list-status//nz-select)[1]")))
        self.driver.execute_script("arguments[0].scrollLeft += 500;", status)
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//worklenz-task-list-row//worklenz-task-list-priority//nz-select)[1]"))).click()
        priority_option = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-option-container//cdk-virtual-scroll-viewport//nz-option-item[3]")))
        priority_text = priority_option.text
        #print(f"Selected phase: {priority_text}")
        priority_option.click()
        time.sleep(5)

        Updated_priority = self.wait.until(EC.visibility_of_element_located
                                        ((By.XPATH, "(//worklenz-task-list-row//worklenz-task-list-priority//nz-select//nz-select-top-control//nz-select-item)[1]"))).text
        #print(Updated_priority)

        if priority_text in Updated_priority:
            print("Test passed:")

        else:
            print("Test failed:")

    def verify_log_time_for_the_task(self):
        self.enter_data_to_login(self.wait, "hello23@gmail.com", "heLLo12@")
        self.open_a_project(self.wait)
        status = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "worklenz-task-list-status")))
        self.driver.execute_script("arguments[0].scrollLeft += 2500;", status)
        timer = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//worklenz-task-timer//button")))
        timer.click()
        time.sleep(15)
        timer.click()
        time.sleep(5)

        taskName_element = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                           "(//div[@class='inner-task-name-container']//div[contains(@class, 'task-name-text')])[1]")))
        ActionChains(self.driver).move_to_element(taskName_element).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "(//span[normalize-space()='Open'])[1]"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Time Log')]"))).click()





