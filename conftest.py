
from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def driver_setup(request):
    web_driver = webdriver.Chrome(executable_path='drivers/linux/chromedriver')
    request.cls.driver = web_driver
    yield
    web_driver.close()



"""   #teardown(request)


#def teardown(request):
#   request.browser.close()
#   request.browser.quit()
"""