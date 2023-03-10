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


class TestLoginPageNegative(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system_negative(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("TOst-1294")
        user_login.click_on_the_sign_in_button()
        scouts_panel = self.driver.find_element(By.XPATH, '//*[@id="__next"]/form/div/div[1]/div[3]/span')
        assert scouts_panel.text == 'Identifier or password invalid.'
        print("'Identifier or password invalid.' title is fine")
        time.sleep(5)



    @classmethod
    def tearDown(self):
        self.driver.quit()
