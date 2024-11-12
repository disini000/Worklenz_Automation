import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from faker import Faker

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.faker = Faker()

    def enter_data_to_login(self, wait, username, password):
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Email']"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))).send_keys(password)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

    def create_new_project(self):

        project_details = {
            "project_name": "",
            "status": "",
            "health": "",
            "category": "",
            "note": "",
            "client": "",
            "working_days": "",
            "mans_days": ""

        }

        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")

        project_name = self.faker.name()
        project_details["project_name"] = project_name + "'s project"

        status_options = ["Cancelled", "Blocked", "On Hold", "Proposed", "In Planning", "In Progress","Completed"]
        random_number_status = self.faker.random_int(min=0, max=6)
        project_details["status"] =  status_options[random_number_status]

        health_options = ["Not Set", "Needs Attention", "At Risk", "Good"]
        random_number_health = self.faker.random_int(min=0, max=3)
        project_details["health"] = health_options[random_number_health]

        note = self.faker.sentence()
        project_details["note"] = note
        client_name = self.faker.name()
        project_details["client"] = client_name
        project_details["working_days"] = 44
        project_details["mans_days"] = 44

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Create Project']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Name']"))).send_keys(
            project_name + "'s project")

        # select_colour
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "rounded-circle"))).click()
        time.sleep(3)
        colors = self.wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//div[@class='cdk-overlay-connected-position-bounding-box']//li")))
        print(len(colors))
        # colors = color_dropdown.find_elements(By.TAG_NAME, 'li')
        random_color_number = self.faker.random_int(min=0, max=24)
        print(len(colors))
        no = random_color_number
        colors[no].click()

        # select_status
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-form-item[3]//nz-form-control//nz-select"))).click()
        status_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")))
        status = status_dropdown.find_elements(By.TAG_NAME, 'nz-option-item')
        status[random_number_status].click()
        time.sleep(3)

        # select_health
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-form-item[4]//nz-form-control//nz-select"))).click()
        health_dropdown = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")))
        health = health_dropdown.find_elements(By.TAG_NAME, 'nz-option-item')
        health[random_number_health].click()
        time.sleep(3)

        # select_category
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//worklenz-project-categories-autocomplete//nz-form-item//nz-form-control//nz-select"))).click()
        elements = self.driver.find_elements(By.TAG_NAME, "nz-option-item")
        if len(elements) > 2:
            elements[1].click()

        else:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='New Category']"))).click()

        category_options = ["Testing", "Development"]
        project_details["category"] = elements[1].text

        # select_Note & client
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ant-input[placeholder='Notes']"))).send_keys(
            note)
        select_client = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Select client']")))
        select_client.send_keys(client_name)
        time.sleep(3)

        self.driver.execute_script("arguments[0].scrollIntoView();", select_client)

        # select_projectManager
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "nz-avatar.ant-avatar.avatar-dashed"))).click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//li[@class='m-0 ant-dropdown-menu-item ng-star-inserted'])[1]"))).click()

        # select_date = self.wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='ng-tns-c802749266-112 ant-picker-input ng-star-inserted'])[1]")))
        # select_date.click()

        # Estimated_hours
        hours_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-input-number[@placeholder='Estimated Working Days']")))
        hours_input_wait = WebDriverWait(hours_input, 20)
        clear_hours_input = hours_input_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        clear_hours_input.clear()
        clear_hours_input.send_keys("44")
        time.sleep(3)

        # Man_hours
        man_hours = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//nz-input-number[@placeholder='Estimated Man Days']")))
        man_hours_wait = WebDriverWait(man_hours, 20)
        clear_man_hours = man_hours_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
        clear_man_hours.clear()
        clear_man_hours.send_keys("44")
        time.sleep(3)

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block ng-star-inserted']"))).click()
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Projects']"))).click()

        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        project_lists = t_body.find_elements(By.TAG_NAME, "tr")
        for project_list in project_lists:
            project_name_element = project_list.find_elements(By.TAG_NAME, "td")[0]
            if project_details["project_name"] in project_name_element.text:
                project_name_element.click()
                time.sleep(5)
                self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[nz-icon][nztype='setting']"))).click()

                # Verify project details
                form_values = {
                    "project_name": self.wait.until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Name']"))).get_attribute('value'),
                    "status": self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH, "//nz-form-item[4]//nz-form-control//nz-select//nz-select-item"))).get_attribute('title'),
                    "health": self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH, "//nz-form-item[5]//nz-form-control//nz-select//nz-select-item"))).get_attribute('title'),
                    "category": self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH,  "//worklenz-project-categories-autocomplete//nz-form-item//nz-form-control//nz-select//nz-select-item"))).get_attribute('title'),
                    "note": self.wait.until(EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "textarea[placeholder='Notes']"))).get_attribute('value'),
                    "client": self.wait.until(EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "input[placeholder='Select client']"))).get_attribute('value'),
                    "working_days": self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH, "//nz-input-number[@placeholder='Estimated Working Days']//input"))).get_attribute('value'),
                    "mans_days": self.wait.until(EC.visibility_of_element_located(
                        (By.XPATH, "//nz-input-number[@placeholder='Estimated Man Days']//input"))).get_attribute('value'),
                }
                print(project_details)
                print(form_values)

                # Compare the values
                for key in project_details:
                    expected_value = str(project_details[key])
                    actual_value = str(form_values[key])

                    if actual_value == expected_value:
                        print(f"{key} verified.")
                    else:
                        print(f"{key} mismatch.")
                break
        else:
            print(f"Test failed: New project name '{project_details['project_name']}' not found in the table.")


    def add_task_to_ToDoLists(self):
        is_task = False
        task_name = self.faker.sentence()
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='card-data']//input[@placeholder='+ Add Task']"))).send_keys(task_name+ Keys.RETURN)
        time.sleep(3)

        table = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[2]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[1]
            if task_name in task_cell.text:
                print(f"Test passed: New task name '{task_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")


    def add_task_to_the_project(self):
        is_task = False
        task_name = self.faker.word()
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//worklenz-tasks-table[@class='ng-star-inserted']//input[@placeholder='+ Add Task']"))).send_keys(task_name + Keys.TAB)
        due_date = self.wait.until(EC.presence_of_element_located((By.XPATH, "//nz-option-item[@title='Tomorrow']")))
        due_date.click()
        select_project = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='cdk-overlay-7']/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]")))
        project_name = select_project.get_attribute('title')
        select_project.click()
        time.sleep(5)

        table = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[1]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[0]
            project_cell = row.find_elements(By.TAG_NAME, "td")[1]
            if task_name in task_cell.text and project_name in project_cell.text  :
                print(f"Test passed: New task name '{task_name}' and '{project_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")

    def filter_task_with_assign_by_me(self):
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//worklenz-my-tasks/div[1]//nz-space/div[2]/nz-select"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-option-container//nz-option-item[2]"))).click()

        time.sleep(5)

    def filter_tasks_with_ToDay(self):
        is_task = False
        task_name = self.faker.word()
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH,"//worklenz-tasks-table[@class='ng-star-inserted']//input[@placeholder='+ Add Task']"))).send_keys(task_name + Keys.TAB)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//nz-option-item[@title='Today']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='cdk-overlay-7']/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]"))).click()
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-my-tasks//nz-tabset//nz-tabs-nav//div[2]/div"))).click()

        table = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[1]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[0]
            print(task_cell.text)
            if task_name in task_cell.text :
                print(f"Test passed: New task name '{task_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")

    def filter_tasks_with_Upcoming(self):
        is_task = False
        task_name = self.faker.word()
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH,"//worklenz-tasks-table[@class='ng-star-inserted']//input[@placeholder='+ Add Task']"))).send_keys(task_name + Keys.TAB)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//nz-option-item[@title='Next Week']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='cdk-overlay-7']/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]"))).click()
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-my-tasks//nz-tabset//nz-tabs-nav//div[3]/div"))).click()

        table = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[1]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[0]
            print(task_cell.text)
            if task_name in task_cell.text:
                print(f"Test passed: New task name '{task_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")


    def filter_tasks_with_Overdue(self):
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-my-tasks//nz-tabset//nz-tabs-nav//div[4]/div"))).click()

        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-table[@class='ant-table-wrapper mt-2 ng-star-inserted']//table")))
            print("Test passed: filter_tasks_with_Overdue")
        except NoSuchElementException:
            pytest.fail("Test case fail : filter_tasks_with_Overdue")

    def filter_tasks_with_NoDueDate(self):
        is_task = False
        task_name = self.faker.word()
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH,"//worklenz-tasks-table[@class='ng-star-inserted']//input[@placeholder='+ Add Task']"))).send_keys(task_name + Keys.TAB)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//nz-option-item[@title='No Due Date']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='cdk-overlay-7']/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]"))).click()
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//worklenz-my-tasks//nz-tabset//nz-tabs-nav//div[5]/div"))).click()
        time.sleep(2)

        table = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[1]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[0]
            print(task_cell.text)
            if task_name in task_cell.text:
                print(f"Test passed: New task name '{task_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")

    def Add_Project_to_Favorites(self):
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//worklenz-my-projects//nz-table//tr[1]/td//nz-rate//li"))).click()
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//nz-segmented)[2]//label[2]"))).click()
        time.sleep(4)

        try:
            self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//nz-table//tr/td/div/nz-space/div[2]/span")))
            print("Test passed: Add_Project_to_Favorites")
        except NoSuchElementException:
            pytest.fail("Test case fail :Add_Project_to_Favorites")

    def Add_Add_Task_to_a_Project_Using_Calendar_tab(self):
        task_name = self.faker.word()
        is_task = False
        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//nz-segmented)[1]//label[2]"))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'26')]"))).click()
        time.sleep(2)

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//input[@placeholder='+ Add Task'])[1]"))).send_keys(task_name + Keys.TAB)
        select_project = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                         "//*[@id='cdk-overlay-7']/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]")))
        project_name = select_project.get_attribute('title')
        select_project.click()
        time.sleep(5)

        table = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "nz-table-inner-default")))
        to_do_table = table[1]

        rows = to_do_table.find_elements(By.TAG_NAME, "tr")
        print(len(rows))

        for row in rows:
            task_cell = row.find_elements(By.TAG_NAME, "td")[0]
            project_cell = row.find_elements(By.TAG_NAME, "td")[1]
            print(f"Task: {task_cell.text}, Project: {project_cell.text}")
            if task_name in task_cell.text and project_name in project_cell.text:
                print(f"Test passed: New task name '{task_name}' and '{project_name}' found in the table.")
                is_task = True
                break

            if is_task:
                pass
            else:
                pytest.fail(f"Test failed: New task name '{task_name}' not found in the table.")

    def create_new_project_by_importing_templates(self):

        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//nz-button-group/button[2]/span"))).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"span[nz-icon][nztype='import']"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//nz-tabset//worklenz-template-list//ul/li[1]"))).click()

        phase_options = ["Incoming", "Backlog", "Development work", "Resolved", "Testing & Review"]
        status_options = ["To Do", "Doing", "Done"]
        label_options = ["UI/UX Bug", "Ready for Dev", "Regression", "Critical", "Awaiting review", "Fixed", "Duplicate", "Documentation", "Fixing"]
        #task_options = ["Testing and Verification", "Bug Prioritization", "Bug reporting", "Bug Assignment", "Bug Closure", "Documentation ", "Reporting"]
        task_options = ['Bug Closure', 'Testing and Verification', 'Bug Prioritization', 'Reporting', 'Bug reporting', 'Documentation', 'Bug Assignment']

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Create']"))).click()
        time.sleep(5)

    #caputure Status
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//worklenz-task-list-row[1]//worklenz-task-list-status//nz-select)[1]"))).click()

        status_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//cdk-virtual-scroll-viewport")))

        status_items = status_element.find_elements(By.TAG_NAME, "nz-option-item")

        list_texts = []
        for item in status_items:
            item_text = item.text.strip()
            list_texts.append(item_text)

        #print(list_texts)
        if sorted(list_texts) == sorted(status_options):
            print("All status found in the project:")
        else:
            print("Mismatch found:")

    #filter project table to phase to capture phase
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//worklenz-project-view//worklenz-task-list-filters//button[6]"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='ant-typography'][normalize-space()='Phase']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//worklenz-task-list-filters//button[7]"))).click()
        time.sleep(5)

        phase_values = []
        for i in range(1, 6):
            phase_input = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//nz-form-item[{i}]/div/div/nz-form-control/div/div/div/input"))).get_attribute('value')
            phase_values.append(phase_input)

        #print(phase_values)
        if sorted(phase_values) == sorted(phase_options):
            print("All phases found in the project.")
        else:
            print("Mismatch found.")

        time.sleep(5)

    #close_button
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[3]"))).click()
        #label_checking
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//worklenz-task-list-filters//button[4]"))).click()

        ul_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'ant-dropdown-menu')]")))
        nz_menu_items = ul_element.find_elements(By.TAG_NAME, "li")

        list_texts = []
        for item in nz_menu_items[1:]:
            badge_text_element = WebDriverWait(item, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-badge-status-text")))
            badge_text = badge_text_element.text
            list_texts.append(badge_text)  # Append the badge text to the list

        #print(list_texts)
        if sorted(list_texts) == sorted(label_options):
            print("All matches found:")
        else:
            print("Mismatch found:")

    #capture tasks
        task_rows = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))

        list_task_names = []
        for row in task_rows:
            task_name_element = WebDriverWait(row, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "task-name-text")))
            task_name = task_name_element.text.strip()
            list_task_names.append(task_name)

        #print(list_task_names)
        if sorted(list_task_names) == sorted(task_options):
            print("All tasks found in the project:")
        else:
            print("Mismatch found:")






















    def open_project(self):

        self.enter_data_to_login(self.wait, "hello123@gm.com", "heLLo12@")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//strong[text()='Projects']"))).click()
        time.sleep(1)
        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        row_1 = t_body_wait.until(EC.visibility_of_all_elements_located((By.XPATH, "tr")))[1]
        rows_wait = WebDriverWait(row_1, 10)
        rows_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "td")))[0].click()
        time.sleep(5)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//worklenz-task-list-row[1]//worklenz-task-list-status//nz-select)[1]"))).click()

        status_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//cdk-virtual-scroll-viewport")))

        status_items = status_element.find_elements(By.TAG_NAME, "nz-option-item")

        list_texts = []

        for item in status_items:
            item_text = item.text.strip()
            list_texts.append(item_text)

        print(list_texts)

        status_options = ["To Do", "Doing", "Done"]
        if sorted(list_texts) == sorted(status_options):
            print("All matches found:")
        else:
            print("Mismatch found:")




















































