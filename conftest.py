
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def driver_setup(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()



"""   #teardown(request)


#def teardown(request):
#   request.browser.close()
#   request.browser.quit()
"""