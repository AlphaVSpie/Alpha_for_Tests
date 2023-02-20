import os
import unittest
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPassword
from selenium.webdriver.common.by import By
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPassword(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.click_on_remind_password()
        remind_password = RemindPassword(self.driver)
        remind_password.title_of_page()
        remind_password.type_in_email("user01@getnada.com")
        remind_password.click_send()
        remind_password.message_sent()
        time.sleep(5)


    @classmethod
    def tearDown(self):
        self.driver.quit()
