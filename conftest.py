import allure
from allure_commons.types import AttachmentType
from allure_pytest import *
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver_setup(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    if request.node.rep_call.failed:
        try:
            web_driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(web_driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass
    web_driver.close()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


""""@pytest.fixture
def attach_file(png_file):
    allure.attach.file(png_file, attachment_type=pytest.alllure.attachment_type.PNG)"""

"""   #teardown(request)


#def teardown(request):
#   request.browser.close()
#   request.browser.quit()
"""
