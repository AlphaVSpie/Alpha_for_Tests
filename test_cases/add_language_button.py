import os
import unittest
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.base_page import BasePage
from pages.add_a_player import AddPlayer
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from selenium.webdriver.common.by import By
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddLanguageButton(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_language(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait()
        dashboard_page.click_add_a_player()
        add_a_player_page = AddPlayer(self.driver)
        add_a_player_page.title_of_page()
        add_a_player_page.click_add_language()
        add_a_player_page.visibility()
        time.sleep(5)

        print("Languages is shown")

    @classmethod
    def tearDown(self):
        self.driver.quit()