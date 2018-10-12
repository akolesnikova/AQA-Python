from variables import *
from PageObject.LoginPage import LoginPage
from PageObject.CreateIssue import CreateIssue
from PageObject.Update_issue import UpdateIssue
from PageObject.Search_issue_page import SearchIssuePage
import pytest



@pytest.mark.usefixtures('driver_setup')
class TestJira:

    @pytest.mark.parametrize("login,passwd,res", [
        ("web", "web", "please try again"),
        ("Nastya", "Nastya", "please try again"),
        ("webinar5", "webinar5", "System Dashboard")

    ])
    def test_ui_login_to_jira(self, login, passwd, res):
        self.driver.get(ui_url)

        login_page = LoginPage(self.driver)
        login_page.fill_login(login)
        login_page.fill_passwd(passwd)
        login_page.press_loginbtn()
        assert res in login_page.wait_for_result(res)

    @pytest.mark.parametrize("summary,description,res", [
        ('', 'good description', 'You must specify a summary of the issue.'),
        (long_summary, 'good description', "summary: Summary must be less than 255 characters."),
    ])
    def test_ui_create_issue(self, summary, description, res):
        self.driver.get(ui_url + 'secure/CreateIssue!default.jspa?' + 'os_username=webinar5&os_password=webinar5')
        create_issue_page = CreateIssue(self.driver)
        create_issue_page.click_next_btn()
        create_issue_page.fill_summary(summary)
        create_issue_page.fill_description(description)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
        create_issue_page.submit_form()
        create_issue_page.wait_for_result(res)
        assert res in create_issue_page.wait_for_result(res)

    @pytest.mark.parametrize("summary,priority,assignee,issue_id,res", [
        ('Very good Summary', '', '', 'WEBINAR-1052', 'WEBINAR-1052 has been updated.'),
        ('Very good Summary', 'High', '', 'WEBINAR-1052', 'WEBINAR-1052 has been updated.'),
        ('Very good Summary', '', 'webinar5', 'WEBINAR-1052', 'WEBINAR-1052 has been updated.'),
        ])
    def test_ui_update_issue(self, summary, priority, assignee, issue_id, res):
        self.driver.get(ui_url + 'browse/' + issue_id + '?' + 'os_username=webinar5&os_password=webinar5')
        update_issue_page = UpdateIssue(self.driver)
        update_issue_page.press_editbtn()
        update_issue_page.fill_summary(summary)
        update_issue_page.select_priority(priority)
        update_issue_page.select_assignee(assignee)
        update_issue_page.press_updatebtn()
        assert res in update_issue_page.wait_for_result(res)

    @pytest.mark.parametrize("jql,count", [
        ('assignee%20%3D%20webinar5%20AND%20project%20%3D%20AQAPython', 8),
        ('assignee%20%3D%20a.maerskaya%20AND%20project%20%3D%20Sokolova', 1),
        ])
    def test_search_issue(self, jql, count):
        self.driver.get(ui_url + '?' + 'os_username=webinar5&os_password=webinar5')
        self.driver.get(ui_url + 'issues/?jql=' + jql)
        search_issue = SearchIssuePage(self.driver)
        assert count == search_issue.get_count_of_issues()

    @pytest.mark.xfail
    @pytest.mark.parametrize("jql,count", [
        ('assignee%20%3D%20a.maerskaya%20AND%20project%20%3D%20Webinar', 0),

    ])
    def test_find_none_issue(self, jql, count):
        self.driver.get(ui_url + '?' + 'os_username=webinar5&os_password=webinar5')
        self.driver.get(ui_url + 'issues/?jql=' + jql)
        search_issue = SearchIssuePage(self.driver)
        assert count == search_issue.get_count_of_issues()



    """def test_delete_issue(self):
            requests.request('GET', api_search_issue, auth=(user, password), headers=jira_headers)
            return

    def test_delete_issue():
        x = requests.get(api_search_issue, auth=(user, password), headers=jira_headers).json()

    x = json.dumps(x)
    loaded_r = json.loads(x)
    print(loaded_r['self'])  # Output 3.5
    type(x)  # Output str
    type(loaded_r)  # Output dict
    d2 = json.loads(s1)
    print(d2['id'])"""




