from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.wrappers import WrapperFunctions


class HomeScreen(WrapperFunctions):

    def __init__(self, driver):
        super(HomeScreen, self).__init__(driver)
        # self.driver = driver
        self.search_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, 'search')))

    # @allure.step('entering data in textbox')
    def enter_text_in_searchbox(self, search_text):
        # self.search_box.send_keys(search_text + Keys.RETURN)
        self.enter_text(search_text, 'search', 'name')
        self.search_box.send_keys(Keys.RETURN)

        # with allure.step('entering data in textbox'):
        #     allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
