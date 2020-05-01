from PythonPOMSeleniumFW.Locators.locator import Locators
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username_txt_box = Locators.username_txt
        self.password_txt_box = "txtPassword"
        self.login_btn = "btnLogin"

    def login(self, username, password):
        self.driver.find_element_by_id(self.username_txt_box).clear()
        self.driver.find_element_by_id(self.username_txt_box).send_keys(username)
        self.driver.find_element_by_id(self.password_txt_box).clear()
        self.driver.find_element_by_id(self.password_txt_box).send_keys(password)
        self.driver.find_element_by_id(self.login_btn).click()
