from PageObject.BasePage import BasicPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UpdateIssue(BasicPage):
    DESCR_INPUT = (By.ID, "description")
    SUMMARY_INPUT = (By.ID, "summary")
    PRIORITY_INPUT = (By.ID, "priority-field")
    ASSIGNEE_INPUT = (By.ID, "assignee-field")
    UPDATE_BTN = (By.ID, "edit-issue-submit")
    EDIT_BTN = (By.ID, "edit-issue")

    def press_editbtn(self):
        self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN)).click()

    def fill_summary(self, value):
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).clear()
        self.wait.until(EC.visibility_of_element_located(self.SUMMARY_INPUT)).send_keys(value)

    def select_assignee(self, value):
        self.wait.until(EC.visibility_of_element_located(self.ASSIGNEE_INPUT)).send_keys(value)

    def select_priority(self, value):
        self.wait.until(EC.visibility_of_element_located(self.PRIORITY_INPUT)).send_keys(value)

    def press_updatebtn(self):
        self.wait.until(EC.visibility_of_element_located(self.UPDATE_BTN)).click()

    def wait_for_result(self, result):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(.,'" + result + "')]"))).text
