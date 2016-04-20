import unittest
from selenium import webdriver
from Pages.HomePage import HomePage

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        fp = webdriver.FirefoxProfile('C:/Profiles')
        cls.driver = webdriver.Firefox(fp)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.kinztut.com")
        cls.driver.maximize_window()
        HomePage.Login_Homepage(cls)

    @classmethod
    def TearDown(self):
        self.driver.close()


class BaseTestCase_Login(unittest.TestCase):
    @classmethod
    def setUp(cls):
        fp = webdriver.FirefoxProfile('C:/Profiles')
        cls.driver = webdriver.Firefox(fp)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://www.kinztut.com")
        cls.driver.maximize_window()
        HomePage.Login_Homepage(cls)

    @classmethod
    def TearDown(self):
        HomePage.Logout_Homepage(cls)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
