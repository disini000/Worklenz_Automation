
import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


















# @pytest.fixture(scope="class")
# def driver(request):
#     browser = ReadConfig.read_configuration("basic info","driver")
#     driver = None
#     if browser.__eq__("chrome"):
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=options)
#     elif browser.__eq__("firefox"):
#         driver = webdriver.Firefox()
#     elif browser.__eq__("edge"):
#         options = webdriver.EdgeOptions()
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Edge()
#     else:
#         print("Provide a valid browser name")
#
#     wait = WebDriverWait(driver, 12)
#     app_url = ReadConfigurations.read_configuration("basic info","url")
#     driver.get( app_url)
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.cls.faker = Faker()
#     yield driver
#     driver.quit()
