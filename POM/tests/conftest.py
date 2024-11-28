import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def init_driver(request):
    driver = None
    if request.param == "chrome":
        driver = webdriver.Chrome()  
    elif request.param == "firefox":
        driver = webdriver.Firefox()  
    request.cls.driver = driver  

    yield driver  

    driver.quit()  