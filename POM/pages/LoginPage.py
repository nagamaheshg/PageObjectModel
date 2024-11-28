from selenium.webdriver.common.by import By
from config.config import TestData
from pages.BasePage import BasePage

class LoginPage(BasePage):
    Email = (By.ID, "identifierId")
    NEXT = (By.XPATH,"//*[contains(text(),'Next')]")
    PASSWORD = (By.NAME, "Passwd")
    SIGN_IN = (By.XPATH,"//*[contains(text(),'Sign in')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        
    def get_login_page_title(self):
        return self.get_title()
    
    def do_login(self, username, password):
        self.do_send_keys(self.Email, username)
        self.do_click(self.NEXT)  
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGN_IN)