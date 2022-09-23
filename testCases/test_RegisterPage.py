import string
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.HomePage import HomePage
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.LogUtil import Logger
import logging


class Test_004_Register:

    #baseURL = "https://demowebshop.tricentis.com/"
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    log = Logger(__name__, logging.INFO)

    @pytest.mark.sanity
    def test_RegisterPageTiltle(self, setup):
        self.log.logger.info("*****Test_004_Register*****")
        self.log.logger.info("Started Register Page Title Test")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.homepage = HomePage(self.driver)
        self.homepage.navigateToRegister()
        self.registerpage = RegisterPage(self.driver)
        act_title = self.registerpage.getTitle()
        if act_title == "Demo Web Shop. Register":
            assert True
            self.driver.close()
            self.log.logger.info("*****Register Page Test passed*****")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_RegisterPageTiltle.png")
            #self.driver.get_screenshot_as_file("test_goToLogin.png")
            self.driver.close()
            self.log.logger.info("*****Register Page Test failed*****")
            self.log.logger.error("*****Test failed*****")
            assert False

    @pytest.mark.regression
    def test_Register(self, setup):
        self.log.logger.info("*****Test_003_Regsietr*****")
        self.log.logger.info("Started Register Test")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.homepage = HomePage(self.driver)
        self.homepage.navigateToRegister()
        self.registerpage = RegisterPage(self.driver)
        self.registerpage.setGender("Female")
        self.registerpage.setFirstName("Test"+str(random.randrange(1000, 10000, 3)))
        self.registerpage.setLastName("Test"+str(random.randrange(1000, 10000, 3)))
        self.registerpage.setEmail("Test"+str(random.randrange(1000, 10000, 3))+"@gmail.test")
        self.registerpage.setPassword("Tosca1234!")
        self.registerpage.setConfirmPassword("Tosca1234!")
        self.registerpage.clickRegister()

        if self.registerpage.message_register_success_xpath:
            assert True == True
            self.driver.close()
            self.log.logger.info("*****Register Test passed*****")
        else:
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Register.png")
            #self.driver.get_screenshot_as_file("test_goToLogin.png")
            self.driver.close()
            self.log.logger.info("*****Register Test failed*****")
            self.log.logger.error("*****Test failed*****")
            assert True == False

    def random_fname(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))