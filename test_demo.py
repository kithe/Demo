import random
import platform
import unittest
import pytest
import allure
from allure.constants import AttachmentType
from selenium import webdriver
from Engine.SeleniumAction import SeleniuAction
from Engine.CommonMethods import CommonMethods


class SportLight(unittest.TestCase, SeleniuAction, CommonMethods):

    def setUp(self):

        desired_cap = {
            'platform': "Windows 10",
            'browserName': "firefox",
            'version': "58",
            'screenResolution': "1680x1050"
        }
        self.driver = webdriver.Remote(
            command_executor='http://sso-quest-Kit.He:8e360916-121a-4533-b10b-7920986befd8@ondemand.saucelabs.com:80/wd/hub/',
            desired_capabilities=desired_cap)
        allure.environment(PlatformNumber=platform.platform(),
                           BrowserName=self.driver.capabilities['browserName'],
                           BrowserVersion=self.driver.capabilities['browserVersion'],
                           PageLoadStrategy=self.driver.capabilities['pageLoadStrategy']
                           )
        self.driver.implicitly_wait(60)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)
        self.sportLightLogin()

    def tearDown(self):
        self.driver.quit()

    @allure.feature('Feature 1. Spotlight home page nevigation menu.')
    @allure.story('Story 1. As a user,I can nevigate to waitopedia page if i need.')
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.allure.testcase('http://my.tms.org/TESTCASE-1')
    @pytest.allure.step
    def test_a1_navigte_to_page_Waitopedia(self):
        # scan waitopedia page
        with pytest.allure.step('Step1. Click on menu waitopedia.'):
            self.clickOnElement(r"//a[@href='/waitopedia']")

        with pytest.allure.step('Step2. Print the title return from webdriver.'):
            self.waitForTitleIsExpected("Waitopedia | Spotlight")
            print("Current page title is :" + self.driver.title)

        with pytest.allure.step("Step3. Check whether the expected title is equal to actual title."):
            assert self.driver.title == "Waitopedia | Spotlight"

        with pytest.allure.setp("Step4. Check whether the search box exists"):
            self.waitForElementIsVisible("//*[@id='search-input']")

        with pytest.allure.setp("Step5. Check whether chart of the 5 most common wait types exists"):
            allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            self.waitForElementIsVisible("//div[@id='highcharts-0']")

        # with pytest.allure.step("Step4.Just test for random failures."):
        #     assert random.choice([True, False])

    # @allure.feature('Feature 1. Spotlight home page nevigation menu.')
    # @allure.story('Story 2. As a user,I can nevigate to collectiveiq page if i need.')
    # @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    # @pytest.allure.testcase('http://my.tms.org/TESTCASE-2')
    # @pytest.allure.step
    # def test_a2_navigte_to_page_Collectiveiq(self):
    #     # scan Collectiveiq page
    #     with pytest.allure.step('Step1. Click on menu waitopedia.'):
    #         self.clickOnElement(r"//a[@href='/waitopedia']")
    #
    #     with pytest.allure.step('Step2. Click on menu collectiveiq.'):
    #         self.clickOnElement(r"//a[@href='/public/collectiveiq']")
    #
    #     with pytest.allure.step('Step3. Print the title return from webdriver.'):
    #         self.waitForTitleIsExpected("SQL Server World Data | Spotlight")
    #         print("Current page title is :" + self.driver.title)
    #
    #     with pytest.allure.step("Step4. Check whether the expected title is equal to actual title."):
    #         allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    #         self.stringIsEqual("SQL Server World Data | Spotlight", self.driver.title,
    #                            "Collectiveiq page loaded successfully.")
    #         assert self.driver.title == "SQL Server World Data | Spotlight"

        # with pytest.allure.step("Step5.Just test for random failures."):
        #     assert random.choice([True, False])


if __name__ == '__main__':
    unittest.main()
