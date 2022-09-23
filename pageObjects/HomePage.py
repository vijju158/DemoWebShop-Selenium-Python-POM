from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    # Home Page
    link_Login_xpath = "//a[contains(text(),'Log in')]"
    link_Register_xpath = "//a[contains(text(),'Register')]"
    textbox_signup_xpath = "//input[@id='newsletter-email']"
    button_subscribe_xpath = "//input[@id='newsletter-subscribe-button']"


    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        print(self.driver.title)
        return self.driver.title

    def navigateToLogin(self):
        self.driver.find_element(By.XPATH,self.link_Login_xpath).click()
        #self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def navigateToRegister(self):
        self.driver.find_element(By.XPATH,self.link_Register_xpath).click()