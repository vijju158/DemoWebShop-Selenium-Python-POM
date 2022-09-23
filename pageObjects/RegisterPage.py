from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class RegisterPage:
    # Register Page

    radio_male_xpath = "//input[@id='gender-male']"
    radio_female_xpath = "//input[@id='gender-female']"
    textbox_firstname_xpath = "//input[@id='FirstName']"
    textbox_lasttname_xpath = "//input[@id='LastName']"
    textbox_email_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_confirmpassword_xpath = "//input[@id='ConfirmPassword']"
    button_register_xpath = "//input[@id='register-button']"
    message_register_success_xpath = "//div[contains(text(),'Your registration completed')]"


    def __init__(self,driver):
        self.driver=driver

    def getTitle(self):
        print(self.driver.title)
        return self.driver.title

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.radio_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH,self.radio_female_xpath).click()
        else:
            print("Invalid Gender")

    def setFirstName(self, firstname):
        print(firstname)
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(firstname)
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def setLastName(self, lastname):
        print(lastname)
        self.driver.find_element(By.XPATH, self.textbox_lasttname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_lasttname_xpath).send_keys(lastname)
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def setEmail(self, email):
        print(email)
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(email)
        #self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def setConfirmPassword(self, confirmpassword):
        self.driver.find_element(By.XPATH, self.textbox_confirmpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_confirmpassword_xpath).send_keys(confirmpassword)
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.button_register_xpath).click()
        # self.driver.find_element_by_xpath(self.link_Login_xpath).click()

    def verifyRegisterMessage(self):
        # try except block
        try:
            message = self.driver.find_element(By.XPATH, self.message_register_success_xpath)
            if len(message.text)>0:
                print("Element exist")
                return True
            else:
                print("Element Does not exist")
                return False
            # NoSuchElementException thrown if not present
        except NoSuchElementException as e:
            print("Element does not exist" +e)
