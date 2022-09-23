from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    """
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    """
    if browser=='chrome':
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        print("Launching Chrome Browser")
    elif browser=='edge':
        s = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=s)
        print("Launching Edge Browser")
    else:
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        print("Launching Chrome Browser")
    #driver=webdriver.Chrome()
    #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    #Write code to Delete screenshots
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Demo Web Shop - Tricentis'
    config._metadata['Module Name'] = 'Shopping'
    config._metadata['Tester'] = 'Vijay'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
