from page_objects.HomePage.Home import HomePage
from test_cases.conftest import setup
from utilities.ReadConfigurations import ReadConfig


class TestHome:
    baseUrl = ReadConfig.get_application_url()

    def test_Create_New_project(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.create_new_project()

    def test_Add_task_to_ToDoLists(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.add_task_to_ToDoLists()

    def test_add_task_to_the_project(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.add_task_to_the_project()

    def test_filter_tasks_with_assign_by_me(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.filter_task_with_assign_by_me()

    def test_filter_tasks_with_Today(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.filter_tasks_with_ToDay()

    def test_filter_tasks_with_Upcoming(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.filter_tasks_with_Upcoming()

    def test_filter_tasks_with_OverDue(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.filter_tasks_with_Overdue()

    def test_filter_tasks_with_NoDueDate(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.filter_tasks_with_NoDueDate()

    def test_Add_Project_to_Favorites(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.Add_Project_to_Favorites()

    def test_Add_Task_to_a_Project_Using_Calendar_tab(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.Add_Add_Task_to_a_Project_Using_Calendar_tab()

    def test_create_new_project_by_importing_templates(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.create_new_project_by_importing_templates()











    def test_create_open_projects(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.home = HomePage(self.driver)
        self.home.open_project()









































































