import logging

import pytest
from selenium import webdriver

from core.commons import CommonFunctions
from core.star_logger import star_log

log = star_log(log_level=logging.DEBUG)


# Before context
def pytest_bdd_before_scenario(request, feature, scenario):
    log.info('############ Scenario ==>> ||| ' + scenario.name + ' ||| Started ############')
    # print('########## BEFORE SCENARIO ##############')
    # print(feature.name)


def pytest_bdd_after_scenario(request, feature, scenario):
    log.info('############ Scenario ==>> ||| ' + scenario.name + ' ||| Ended ############')
    # print('########## AFTER SCENARIO  ##############')


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    log.info('############ Executing Step ==>> ||| ' + step.name + ' ||| ############')
    allure.step(step.name)
    # print('########## BEFORE STEP  ##############')


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    log.info('############ Step ==>> ||| ' + step.name + ' ||| Execution completed ############')
    # print('########## AFTER STEP  ##############')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    log.info('############ Error Found on Step Name ==>> ||| ' + step.name + ' ||| ############')
    allure.step(step.name)
    # print('########## STEP ERROR  ##############')


def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    log.info('############ Step Validation Error found on Step Name ==>> ||| ' + step.name + ' ||| ############')
    allure.step(step.name)
    # print('########## VALIDATION ERROR  ##############')


# Fixtures
@pytest.fixture
def driver(request):
    try:
        scenario_name = str(request.node.originalname).replace('test_', '')
        print(scenario_name)
        # print('Feature name ==>> ' + feature.name)
        print('Scenario Outline name ==>> ' + request.node.originalname)
        key_value = CommonFunctions.get_browser_mapping(scenario_name)
        print('key_value ======>>>>> ' + key_value)

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
