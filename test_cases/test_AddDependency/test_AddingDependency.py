from page_objects.Dependency.User_AddDependency import UserDependency
from test_cases.conftest import setup
from utilities.ReadConfigurations import ReadConfig


class TestDependency:
    baseUrl = ReadConfig.get_application_url()

    def test_Add_dependency_to_the_task_In_ToDo(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.add_dependency_to_the_task_In_ToDo()

    def test_Dependency_symbol_appears(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.dependency_symbol_appears()

    def test_Add_multiple_dependency_to_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.add_multiple_dependency_to_the_task()

    def test_delete_Dependency_from_Task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.delete_Dependency_from_Task()

    def test_change_Status_After_Deleting_Dependency(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.change_Status_After_Deleting_Dependency()

    def test_change_task_TO_Done_with_Done_Dependency(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.change_task_TO_Done_with_Done_Dependency()

    def test_change_task_to_Done_when_all_dependencies_are_Done(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.change_task_to_Done_when_all_dependancies_are_Done()

    def test_change_Task_as_Done_when_Dependency_is_in_ToDoing(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.change_Task_as_Done_when_Dependency_is_in_ToDoing()

    def test_change_task_to_Done_when_one_dependency_are_not_Done(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.change_task_to_Done_when_one_of_dependancy_are_not_Done()

    def test_add_same_dependency_to_the_task(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.add_same_dependency_to_the_task()

    def test_add_dependency_to_the_Subtask(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.dependency = UserDependency(self.driver)
        self.dependency.add_dependency_to_the_Subtask()