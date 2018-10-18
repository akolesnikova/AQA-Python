from variables import *
from Jira.json_obj import Json
import pytest
import logging
import requests
import json
from jira.client import JIRA
from jira.exceptions import JIRAError


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass  # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client


@pytest.mark.xfail
def test_with_myself():
    login = 'Anastasiya Medennikova'
    passwd = 'Anastasiya_Medennikova'
    res = 200
    assert res == requests.get(jira_url, auth=(login, passwd)).status_code


@pytest.mark.flaky(reruns=5)
@pytest.mark.parametrize("login,passwd,res", [
    ("webinar5", "webinar5", 200),
    ("Nastya", "Nastya", 401),
    ("Medennikova", "Medennikova", 401)

])
def test_login_to_jira(login, passwd, res):
   assert res == requests.request("GET", jira_url, auth=(login, passwd)).status_code


@pytest.mark.parametrize("file_name,res", [
    ("Create_issue.json", 201),
    ("Create_issue_without_sum.json", 400),
    ("Create_issue_without_key_project.json", 400)
])
def test_create_issue(file_name, res):
    assert res == requests.request("POST", jira_url + 'issue/', data=Json(file_name).read_json(),
                                   headers=jira_headers).status_code


@pytest.mark.parametrize("jql,res", [
    ('issue/AQAPYTHON-4930', 200),
    ('issue/AQAPYTHON-0000', 404),
    ('***/NastyaProject', 404)
])
def test_search_issue(jql, res):
    #temp = requests.get(jira_url + jql, auth=(user, password), headers=jira_headers).json()
    assert res == requests.get(jira_url + jql, auth=(user, password), headers=jira_headers).status_code


@pytest.mark.parametrize("file_name,issue_id,res", [
    ('Update_issue.json', 'AQAPYTHON-5029', 204),
    ('Update_issue_type.json', 'AQAPYTHON-4930', 204),
    ('Update_issue_assignee.json', 'AQAPYTHON-4908', 204),
])
def test_update_issue(file_name, issue_id, res):
    assert res == requests.request("PUT", jira_url + 'issue/' + issue_id, data=Json(file_name).read_json(),
                                   headers=jira_headers).status_code





