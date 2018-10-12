from PageObject.BasePage import BasicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchIssuePage(BasicPage):
    ISSUES_LIST = (By.CSS_SELECTOR, "ol.issue-list li")

    def get_count_of_issues(self):
        return len(self.wait.until(EC.visibility_of_all_elements_located(self.ISSUES_LIST)))