import unittest
from time import sleep

from ddt import ddt,data,unpack

from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.DataSources import read_excel
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


@ddt
class LoginTest(BaseTestCase):

    @data(*read_excel.get_data_from_excel('D:\Automation\Kinztut_Automation_Project\Data\login_data.xlsx','login'))
    @unpack
    def test_login_valid(self,email_address,password):
       LoginPage.login(self,email_address,password)
       sleep(3);
       #self.assertEqual(LoginName,HomePage.get_login_name(self))
       #print(HomePage.get_login_name(self))




if __name__ == '__main__':
    unittest.main()
