import selenium
from selenium.webdriver.common.by import By


class HomePage():
    Login_Button = (By.XPATH,".//*[@id='home']/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[6]/div/a[1]")  # Define Login Button
    Logout_Button = (By.XPATH,"html/body/div[4]/div[1]/div[2]/div/div/div[2]/ul/li[6]/div/a")

    def Login_Homepage(self):
        self.driver.find_element(*HomePage.Login_Button).click()

    def Logout_Homepage(self):
        self.driver.find_element(*HomePage.Logout_Button).click()



