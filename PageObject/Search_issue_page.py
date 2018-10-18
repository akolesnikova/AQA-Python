from PageObject.BasePage import BasicPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchIssuePage(BasicPage):
    ISSUES_LIST = (By.CSS_SELECTOR, "ol.issue-list li")

    def get_count_of_issues(self):
        return len(self.wait.until(EC.visibility_of_all_elements_located(self.ISSUES_LIST)))

    def get_count_of_nnnnone_issues(self, res):
        return res(self.wait.until(EC.invisibility_of_element_located(self.ISSUES_LIST)))

    def get_count_of_none_issues(self, result):
        return self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "ol.issue-list li" + result + "')]")
                                                                  )
                               ).text
