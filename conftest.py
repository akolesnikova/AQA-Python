import allure
from allure_pytest import *
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def driver_setup(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()


""""@pytest.fixture
def attach_file(png_file):
    allure.attach.file(png_file, attachment_type=pytest.alllure.attachment_type.PNG)"""


"""   #teardown(request)


#def teardown(request):
#   request.browser.close()
#   request.browser.quit()
"""