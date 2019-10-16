import logging
from datetime import datetime
from traceback import print_stack

import pytest
from selenium import webdriver

from core.commons import CommonFunctions
from core.star_logger import star_log

log = star_log(log_level=logging.DEBUG)


def pytest_bdd_before_scenario(request, feature, scenario):
    log.info('############ Scenario ==>> ||| ' + scenario.name + ' ||| Started ############')


def pytest_bdd_after_scenario(request, feature, scenario):
    log.info('############ Scenario ==>> ||| ' + scenario.name + ' ||| Ended ############')


def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    log.info('############ Executing Step ==>> ||| ' + step.name + ' ||| ############')


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    log.info('############ Step ==>> ||| ' + step.name + ' ||| Execution completed ############')


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    log.info('############ Error Found on Step Name ==>> ||| ' + step.name + ' ||| ############')


def pytest_bdd_step_validation_error(request, feature, scenario, step, step_func, step_func_args, exception):
    log.info('############ Step Validation Error found on Step Name ==>> ||| ' + step.name + ' ||| ############')


def decorator_screenshot(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError:
            CommonFunctions().take_screenshot(driver, 'Error screenshot')
            raise

    return wrapper


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if CommonFunctions().get_star_json(key_name='TEST_TYPE') == 'WEB':
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('driver')
            if (report.skipped and xfail) or (report.failed and not xfail):
                # print('****************inside snapshot******************************')
                snap = timestamp + '.png'
                snapshot = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(snapshot, ''))
            report.extra = extra


# Fixtures
# def take_screenshot(driver, test_name):
#     screenshots_dir = "././screenshots"
#     screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
#     driver.save_screenshot(
#         screenshot_file_path
#     )


@pytest.fixture
def driver(request):
    if CommonFunctions().get_star_json(key_name='TEST_TYPE') == 'WEB':
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
                print(
                    '### Browser Type NOT mentioned correctly in star.json, defaulting execution with Chrome browser ###')
                d = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

            d.implicitly_wait(10)
            # failed_before = request.session.testsfailed
            yield d
            # if request.session.testsfailed != failed_before:
            #     test_name = request.node.name
            #     take_screenshot(d, test_name)
            d.close()
            d.quit()
        except:
            print_stack()
            print('Error in creating driver instance...')

    elif CommonFunctions().get_star_json(key_name='TEST_TYPE') == 'MOBILE':
        # work in progress | Ravi Salunkhe
        pass
    elif CommonFunctions().get_star_json(key_name='TEST_TYPE') == 'API':
        # work in progress | Ravi Salunkhe
        pass
    elif CommonFunctions().get_star_json(key_name='TEST_TYPE') == 'DB':
        # work in progress | Ravi Salunkhe
        pass

    else:
        pass

# to be added later
# @pytest.fixture
# def get_page_instance(driver):
#
#     home_screen = HomeScreen(driver)
#     result_screen = ResultsScreen(driver)
