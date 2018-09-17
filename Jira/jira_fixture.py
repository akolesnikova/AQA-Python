from Jira.variables import *


@pytest.fixture
def rest():
    response = requests.get(api_url)
    status = response.status_code
    response.json()
    if status == 200:
        print('It works fine')
