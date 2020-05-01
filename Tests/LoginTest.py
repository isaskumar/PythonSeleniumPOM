from selenium import webdriver
import time
import unittest
from PythonPOMSeleniumFW.Pages.LoginPage import LoginPage
from PythonPOMSeleniumFW.Pages.HomePage import HomePage
import HTMLTestRunner


class LoginCrmTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/semmalai/PycharmProjects/SeleniumPythonFramework/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login_crm(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login("Admin", "admin123")
        time.sleep(5)
        homepage = HomePage(driver)
        homepage.logout()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("The Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner("C:/Users/semmalai/PycharmProjects/SeleniumPythonFramework/PythonPOMSeleniumFW/Reports"))
