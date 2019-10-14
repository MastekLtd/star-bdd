from core.wrappers import WrapperFunctions


class ResultsScreen(WrapperFunctions):
    # Page Element Locators
    HEADING_BY_ID = 'firstHeading'

    def __init__(self, driver):
        super(ResultsScreen, self).__init__(driver)

    def verify_header_text(self, text):
        header_text = self.get_element_text(self.HEADING_BY_ID, 'id')
        self.verify_text_equals(actual_text=header_text, expected_text=text)
        print('this is after assert2')
