import os
import unittest
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSingOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_sing_out(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        scouts_panel = self.driver.find_element(By.XPATH, "//*[@id='__next']/form/div/div[1]/h5")
        assert scouts_panel.text == 'Scouts Panel'
        print("'Scouts Panel' title is fine")
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(4)
        dashboard_page.click_sign_out()
        scouts_panel = self.driver.find_element(By.XPATH, "//*[@id='__next']/form/div/div[1]/h5")
        assert scouts_panel.text == 'Scouts Panel'
        print("'Scouts Panel' title is fine")

        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()
