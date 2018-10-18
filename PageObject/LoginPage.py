from selenium.webdriver.support import expected_conditions as EC
from PageObject.BasePage import BasicPage
from selenium.webdriver.common.by import By


class LoginPage(BasicPage):
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASWD_INPUT = (By.ID, "login-form-password")
    LOGIN_BTN = (By.ID, "login")
    JIRA_LOGO = (By.ID, "logo")

    def fill_login(self, value):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_INPUT)).send_keys(value)

    def fill_passwd(self, value):
        self.wait.until(EC.visibility_of_element_located(self.PASWD_INPUT)).send_keys(value)

    def press_loginbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BTN)).click()

    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text
