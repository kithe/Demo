from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium import webdriver

class CommonMethods:
    def sportLightLogin(self):
        self.driver.get("https://testapp.spotlightessentials.com/monitor/groups/heatmap")

        self.inputValue("//input[@id='username']", "questdemo2@gmail.com")

        self.inputValue("//input[@id='password']", "QuestDemo123")

        self.clickOnElement("//button[@id='kc-login']")

        self.element_is_exits("//a[@class='_hj-f5b2a1eb-9b07_transition']",waittime=20, is_need_quit=False)


