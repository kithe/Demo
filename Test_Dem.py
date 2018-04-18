import random
import platform
import unittest
import pytest
import allure
import time
from selenium import webdriver
from Engine.SeleniumAction import SeleniuAction
from Engine.CommonMethods import CommonMethods


class SportLight(unittest.TestCase, SeleniuAction, CommonMethods):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.driver.set_page_load_timeout(60)
        # self.driver.set_script_timeout(60)
        #
        # self.sportLightLogin()

        desired_cap = {
            'platform': "Windows 10",
            'browserName': "microsoftedge",
            'version': "16",
            'screenResolution': "1680x1050"
        }
        self.driver = webdriver.Remote(
            command_executor='http://sso-quest-Kit.He:8e360916-121a-4533-b10b-7920986befd8@ondemand.saucelabs.com:80/wd/hub/',
            desired_capabilities=desired_cap)

        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)

        self.sportLightLogin()

    def tearDown(self):
        self.driver.quit()

    def test_a1_navigte_to_page_Monitoring(self):
        # scan Monitoring page
        self.waitForTitleIsExpected("Monitor")
        print("Current page title is :" + self.driver.title)

        self.waitForElementIsVisible("//div[@id='search']/input[@class='form-control']")

        self.waitForElementIsVisible("//div[@class='heatMapWrapChild']")

    # def test_a2_navigte_to_page_Waitopedia(self):
    #     # scan Waitopedia page
    #     self.clickOnElement(r"//a[@href='/waitopedia']")
    #
    #     self.waitForTitleIsExpected("Waitopedia | Spotlight")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//*[@id='search-input']")
    #
    #     self.waitForElementIsVisible("//div[@id='highcharts-0']")

    # def test_a3_navigte_to_page_Collectiveiq(self):
    #     # scan Collectiveiq page
    #     self.clickOnElement(r"//a[@href='/waitopedia']")
    #
    #     self.clickOnElement(r"//a[@href='/public/collectiveiq']")
    #
    #     self.waitForTitleIsExpected("SQL Server World Data | Spotlight")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//div[@id='highcharts-2']")
    #
    # def test_a4_navigte_to_page_Support(self):
    #     # scan Support page
    #     self.clickOnElement(r"//a[@href='/support']")
    #
    #     self.waitForTitleIsExpected("Support")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//a[@href='http://status.spotlightessentials.com/']")
    #
    # def test_a5_navigte_to_page_Subscriptions(self):
    #     # scan Subscriptions page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@href='/subscriptions']")
    #
    #     self.waitForTitleIsExpected("SpotlightCloudSubscriptionManagementWeb")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//table[@class='data-grid row-border']")
    #
    # def test_a6_navigte_to_page_Profile(self):
    #     # scan Configuration-Profile page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@routerlink='/profile']")
    #
    #     self.waitForTitleIsExpected("Configuration")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//div[@class='user-profile']")
    #
    # def test_a7_navigte_to_page_People(self):
    #     # scan Configuration-People page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@routerlink='/people']")
    #
    #     self.waitForTitleIsExpected("Configuration")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//table[@class='row-border hover ds-table dataTable no-footer']")
    #
    # def test_a8_navigte_to_page_Connections(self):
    #     # scan Configuration-Connections page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@routerlink='/connections']")
    #
    #     self.waitForTitleIsExpected("Configuration")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//table[@class='row-border hover dataTable no-footer']")
    #
    # def test_a9_navigte_to_page_diagnosticServer(self):
    #     # scan Configuration-diagnostic server page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@routerlink='/diagnostic-server']")
    #
    #     self.waitForTitleIsExpected("Configuration")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//table[@class='row-border hover ds-table dataTable no-footer']")
    #
    # def test_b1_navigte_to_page_HealthCheckSettings(self):
    #     # scan Configuration-Health Check Settings page
    #     self.clickOnElement(r"//img[@height='30']")
    #     self.clickOnElement(r"//a[@href='/configuration']")
    #     self.clickOnElement(r"//a[@routerlink='/health-check-settings']")
    #
    #     self.waitForTitleIsExpected("Configuration")
    #     print("Current page title is :" + self.driver.title)
    #
    #     self.waitForElementIsVisible("//table[@class='row-border hover ds-table dataTable no-footer']")


if __name__ == '__main__':
    unittest.main()