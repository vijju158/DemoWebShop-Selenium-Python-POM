from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.HomePage import HomePage
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.LogUtil import Logger
import logging


class Test_001_Home:

    #baseURL = "https://demowebshop.tricentis.com/"
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    log = Logger(__name__, logging.INFO)

    @pytest.mark.sanity
    def test_HomePageTitle(self,setup):
        self.logger.info("*****Test_001_Home*****")
        self.logger.info("Started Home Page title")
        self.log.logger.info("*****Test_001_Home*****")
        self.log.logger.info("Started Home Page title")
        self.driver = setup
        #self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.homepage=HomePage(self.driver)
        act_title=self.homepage.getTitle()
        if act_title=="Demo Web Shop":
            assert True
            self.driver.close()
            self.log.logger.info("Home Page Title Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.log.logger.info("Home Page Title Test Failed")
            self.log.logger.error("Test failed")
            assert False
        #assert act_title == "Demo Web Shop", "Title Not Matching"

    @pytest.mark.sanity
    def test_goToLogin(self, setup):
        self.log.logger.info("*****Test_001_Home*****")
        self.log.logger.info("Started Login Page Test")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.homepage = HomePage(self.driver)
        self.homepage.navigateToLogin()
        self.loginpage = LoginPage(self.driver)
        act_title = self.loginpage.getTitle()
        if act_title == "Demo Web Shop. Login":
            assert True
            self.driver.close()
            self.log.logger.info("Login Page Test passed")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_goToLogin.png")
            #self.driver.get_screenshot_as_file("test_goToLogin.png")
            self.driver.close()
            self.log.logger.info("Login Page Test failed")
            self.log.logger.error("Test failed")
            assert False