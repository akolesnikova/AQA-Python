from PageObject.BasePage import BasicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CreateIssue(BasicPage):
    CREATE_BTN = (By.ID, 'create_link')
    NEXT_BTN = (By.ID, 'issue-create-submit')
    SUMMARY = (By.ID, 'summary')
    DESCRIPTION = (By.ID, 'description')
    PRIORITY = (By.ID, 'priority-field')
    SUBMIT_ISSUE_BTN = (By.ID, 'issue-create-submit')
    ISSUE_NAME = (By.ID, 'summary-val')

    def open_form(self):
        self.wait.until(EC.visibility_of_element_located(self.CREATE_BTN)).click()

    def click_next_btn(self):
        self.wait.until(EC.presence_of_element_located(self.NEXT_BTN)).click()

    def fill_summary(self, value):
        self.wait.until(EC.presence_of_element_located(self.SUMMARY)).send_keys(value)

    def fill_description(self, value):
        self.wait.until(EC.presence_of_element_located(self.DESCRIPTION)).send_keys(value)

    def fill_priority(self):
        self.wait.until(EC.presence_of_element_located(self.PRIORITY)).click()

    def submit_form(self):
        self.wait.until(EC.presence_of_element_located(self.SUBMIT_ISSUE_BTN)).click()

    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text




