import pytest
from selenium import webdriver

from core.commons import CommonFunctions


# Fixtures
@pytest.fixture
def driver(request):
    try:
        scenario_name = str(request.node.originalname).replace('test_', '')
        print(scenario_name)
        key_value = CommonFunctions.get_browser_mapping(scenario_name)
        print('key_value ------>>> ' + key_value)

        if key_value == "CHROME":
            d = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        elif key_value == 'FIREFOX':
            d = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        elif key_value == 'IE':
            d = webdriver.Ie(executable_path='drivers/IEDriverServer.exe')
        else:
            print('### Browser Type NOT mentioned correctly in star.json, defaulting execution with Chrome browser ###')
            d = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

        d.implicitly_wait(10)
        yield d
        d.close()
        d.quit()

    except:
        print('Error in creating driver instance...')

# to be added later
# @pytest.fixture
# def get_page_instance(driver):
#
#     home_screen = HomeScreen(driver)
#     result_screen = ResultsScreen(driver)
