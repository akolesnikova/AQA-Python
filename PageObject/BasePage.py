from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BasicPage(object):
    def __init__(self, driver: WebDriver, ):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        cap = DesiredCapabilities.CHROME
        cap["unexpectedAlertBehaviour"] = "accept"
