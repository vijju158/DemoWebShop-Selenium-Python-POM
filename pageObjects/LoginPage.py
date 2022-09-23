from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page

    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//input[@value='Log in']"


    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        print(self.driver.title)
        return self.driver.title

    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        #self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()