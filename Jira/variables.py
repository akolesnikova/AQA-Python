import time

import pytest
import requests

user = 'webinar5'
password = 'webinar5'
api_url = "http://jira.hillel.it:8080/"
jira_url = "http://jira.hillel.it:8080/rest/api/2/"
jira_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic d2ViaW5hcjU6d2ViaW5hcjU="
}
normal_summary = 'Summary from Anastasiia'
normal_body = 'Description from Anastasiia'
empty_summary = ''
long_summary = 'qweananananananananananananananananananananananananananananananananananananananananananananananananananananananananananana'