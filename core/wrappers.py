##########################################
####
# Description : Wrapper methods for selenium library
# Developer : Ravi Salunkhe(ravi.salunkhe@mastek.com)
# Modified Date : 3rd Oct 2019
####
###########################################


from traceback import print_stack

from selenium.webdriver.common.by import By


class WrapperFunctions():

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT
        elif locator_type == "tag_name":
            return By.TAG_NAME
        else:
            # self.log.info("Locator type : " + locator_type + " not correct or supported")
            print("Locator type : " + locator_type + " not correct or supported")
            return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element found with locator :: " + locator + " and locator_type :: " + locator_type)
        except:
            print("Element NOT found with locator :: " + locator + " and locator_type :: " + locator_type)
        return element

    def enter_text(self, data, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print("Entered " + data + " on element with locator :: " + locator + " and locator_type :: " + locator_type)
        except:
            print(
                "Unable to enter " + data + " in element with locator :: " + locator + " and locator_type :: " + locator_type)
            print_stack()
