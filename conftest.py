
from selenium import webdriver
import pytest
import os, sys, platform


os_name = platform.system().lower()
root_dir = sys.path[0]
extension = ".exe" if "win" in os_name else ""
path_to_driver = os.path.join(root_dir, "driver", "chromedriver" + extension)


@pytest.fixture(scope='class')
def driver_setup(request):
    web_driver = webdriver.Chrome(executable_path=path_to_driver)
    request.cls.driver = web_driver
    yield
    web_driver.close()



"""   #teardown(request)


#def teardown(request):
#   request.browser.close()
#   request.browser.quit()
"""