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


class TestEmptyField(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_empty_req_field(self):
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
        add_a_player_page.type_in_name('Don')
        add_a_player_page.click_surname()
        add_a_player_page.type_in_age('26.07.1996')
        add_a_player_page.type_in_main_position('Forward')
        add_a_player_page.click_district()
        add_a_player_page.click_opole()
        add_a_player_page.click_add_language()
        add_a_player_page.type_in_languages("English")
        add_a_player_page.click_submit()
        surname = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/p')
        assert surname.text == 'Required'
        print("'Required' title is fine")

        time.sleep(5)

        print("SUCCESS")

    @classmethod
    def tearDown(self):
        self.driver.quit()