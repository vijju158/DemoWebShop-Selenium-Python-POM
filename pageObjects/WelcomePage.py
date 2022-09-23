from selenium import webdriver
from selenium.webdriver.common.by import By


class WelcomePage:
    # Welcome Page

    link_Logout_xpath = "//a[contains(text(),'Log out')]"


    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        print(self.driver.title)
        return self.driver.title

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_Logout_xpath).click()
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()