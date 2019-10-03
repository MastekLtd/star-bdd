from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ResultsScreen():

    def __init__(self, driver):
        self.driver = driver
        self.header_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstHeading')))

    # @allure.step('verify header text')
    def verify_header_text(self, text):
        assert self.header_text.text == text
        # with allure.step('verify header text'):
        #     allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
