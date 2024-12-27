from page_objects.ProjectInside.tasklist import ProjectInside
from test_cases.conftest import setup
from utilities.ReadConfigurations import ReadConfig


class TestProjectInside:
    baseUrl = ReadConfig.get_application_url()

    def test_UI_elements_in_tasklist(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.Verify_UI_Elements_in_Tasklist()

    # def test_Tooltips_in_Tasklist(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.projectInside = ProjectInside(self.driver)
    #     self.projectInside.Verify_Tooltips_in_Tasklist()

    def test_task_creation_via_Create_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_task_creation_via_Create_task()

    def test_task_creation_via_Import_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_task_creation_Via_Import_task()

    def test_verify_rename_the_status(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_rename_the_status()

    def test_verify_Change_category(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Change_category()

    def test_verify_Add_a_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Add_a_task()

    def test_verify_Add_a_subtask(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Add_a_subtask()

    def test_verify_Edit_the_task_name(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_edit_the_task()

    def test_verify_Assign_members_to_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Assign_members_to_the_task()

    def test_verify_Add_label_to_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Add_label_to_the_task()

    def test_Change_status_of_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Change_status_of_the_task()

    def test_Change_phase_of_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Change_phase_of_the_task()

    def test_Change_priority_of_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_Change_priority_of_the_task()

    def test_log_time_for_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.projectInside = ProjectInside(self.driver)
        self.projectInside.verify_log_time_for_the_task()
