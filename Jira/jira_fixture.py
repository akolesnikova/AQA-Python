from variables import *


@pytest.fixture
def rest():
    response = requests.get(ui_url)
    status = response.status_code
    response.json()
    if status == 200:
        print('It works fine')
