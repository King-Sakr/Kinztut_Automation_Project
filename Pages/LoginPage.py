from selenium.webdriver.common.by import By


# from Pageobject_Support.Cachable import callable_find_by as find_by from selenium.webdriver.common.by.By


class LoginPage():

    Email_TXT = (By.NAME,'login_email')  # Define Username field
    # text_area.send_keys('Administrator')#Enter Username

    Password_TXT = (By.NAME,'login_pass')  # Define Password field
    # text_area.send_keys('P@ssw0rd')#Enter Password

    Signin_BTN = (By.ID,'customer_login')  # Define Login Button

    def login(self,email_address,password):
        self.driver.find_element(*LoginPage.Email_TXT).send_keys(email_address)
        self.driver.find_element(*LoginPage.Password_TXT).send_keys(password)
        self.driver.find_element(*LoginPage.Signin_BTN).click()
