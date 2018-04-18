from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SeleniuAction:

    def clickOnElement(self, xpath):
        elm = self.waitForElementIsClickable(xpath)
        elm.click()

    def inputValue(self, xpath, text_value):
        elm = self.waitForElementIsVisible(xpath)
        elm.send_keys(text_value)

    def stringIsEqual(self, expected_result, actal_result, msg):
        try:
            self.assertEqual(expected_result, actal_result)
            print(msg)
        except AssertionError as e:
            raise e

    '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
    def waitForElementIsVisible(self, xpath):
        try:
            elm = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except:
            print("Wait for element is time out.")
            self.driver.quit()
        return elm

    '''判断title,返回布尔值'''
    def waitForTitleIsExpected(self, expected_title):
        try:
            WebDriverWait(self.driver, 30).until(EC.title_is(expected_title))
        except:
            print("Title is not expected.")
            self.driver.quit()

    '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
    def waitForElementIsClickable(self, xpath, waittime=30, is_need_quit=True):
        try:
            elm = WebDriverWait(self.driver, waittime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except:
            if is_need_quit:
                print("Wait for element is time out, so quit.")
                self.driver.quit()
            else:
                print("Wait for element is time out.")
        return elm

    # ---------------Debug the window where the login appears.-----------------
    def element_is_exits(self, xpath, waittime=30, is_need_quit=True):
        try:
            elm = WebDriverWait(self.driver, waittime).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            elm.click()
        except:
            if is_need_quit:
                print("Wait for element is time out, so quit.")
                self.driver.quit()
            else:
                print("The feedback popup did not appear after login.")
        # return elm