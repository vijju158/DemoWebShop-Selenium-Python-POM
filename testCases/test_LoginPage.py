from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.HomePage import HomePage
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.LogUtil import Logger
import logging


class Test_002_Login:

    #baseURL = "https://demowebshop.tricentis.com/"
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    log = Logger(__name__, logging.INFO)

    @pytest.mark.sanity
    def test_LoginPageTiltle(self, setup):
        self.log.logger.info("*****Test_002_Login*****")
        self.log.logger.info("Started Login Page Title Test")
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

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Login(self, setup):
        self.log.logger.info("*****Test_002_Login*****")
        self.log.logger.info("Started Login Test")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.homepage = HomePage(self.driver)
        self.homepage.navigateToLogin()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setEmail("vijay.malladi@gmail.test")
        self.loginpage.setPassword("Tosca1234!")
        self.loginpage.clickLogin()

        act_title = self.loginpage.getTitle()
        if act_title == "Demo Web Shop":
            assert True
            self.driver.close()
            self.log.logger.info("Login Test passed")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Login.png")
            #self.driver.get_screenshot_as_file("test_goToLogin.png")
            self.driver.close()
            self.log.logger.info("Login Test failed")
            self.log.logger.error("Test failed")
            assert False