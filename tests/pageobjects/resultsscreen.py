from core.wrappers import WrapperFunctions


class ResultsScreen(WrapperFunctions):

    def __init__(self, driver):
        super(ResultsScreen, self).__init__(driver)
        # self.driver = driver
        # self.header_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'firstHeading')))

    # @allure.step('verify header text')
    def verify_header_text(self, text):
        assert self.get_element_text('firstHeading', 'id') == text
        # with allure.step('verify header text'):
        #     allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
