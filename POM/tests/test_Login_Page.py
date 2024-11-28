import pytest
from config.config import TestData
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest

class Test_LoginPage(BaseTest):
    
    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_login_page_title()
        assert title == TestData.LOGIN_PAGE_TITLE
            
    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        
        