import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.HomePage import HomePage
import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.WelcomePage import WelcomePage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.LogUtil import Logger
import logging


class Test_003_LoginDDT:

    baseURL = ReadConfig.getApplicationURL()
    path = "./TestData/LoginData.xlsx"
    logger=LogGen.loggen()
    log = Logger(__name__, logging.INFO)

    @pytest.mark.regression
    def test_LoginDDT(self, setup):
        self.log.logger.info("*****Test_003_Login DDT*****")
        self.log.logger.info("Started Login Test")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
            print(self.email)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            print(self.password)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            print(self.exp)
            self.homepage = HomePage(self.driver)
            self.homepage.navigateToLogin()
            self.loginpage = LoginPage(self.driver)
            self.loginpage.setEmail(self.email)
            self.loginpage.setPassword(self.password)
            self.loginpage.clickLogin()
            self.welcomepage = WelcomePage(self.driver)
            act_title = self.welcomepage.getTitle()
            exp_title = "Demo Web Shop"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.welcomepage.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    #self.welcomepage.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    self.welcomepage.clickLogout();
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    #self.welcomepage.clickLogout();
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.save_screenshot("..\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  Test_003_LoginDDT ************* ")
