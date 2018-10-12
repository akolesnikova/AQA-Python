from Jira.json_obj import Json
import pytest
import requests

user = 'webinar5'
password = 'webinar5'
ui_url = "http://jira.hillel.it:8080/"
jira_url = "http://jira.hillel.it:8080/rest/api/2/"
jira_headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic d2ViaW5hcjU6d2ViaW5hcjU="
}
normal_summary = 'Summary from Anastasiia'
normal_body = 'Description from Anastasiia'
empty_summary = ''
long_summary = 'Hello, everyone! This is one of the weirdest sites: or your money back! We have ZIM, neopets, music, and much, much, more. E-mail us for questions, comments, complaints and information. Why not click on the Very Weird Stuff link to see more, or click on the music link?'
