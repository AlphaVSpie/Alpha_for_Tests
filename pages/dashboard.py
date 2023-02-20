import time
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    add_player_button_xpath = "//span[normalize-space()='Add player']"
    dashboard_url = 'https://scouts.futbolkolektyw.pl/en'
    Shortcuts = '//*[text()="Shortcuts"]'
    button_Main_Page = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    Reports_count = '//*[text()="Reports count"]'
    activity_xpath = '//*[text()="Activity"]'
    Events_count = '//*[text()="Events count"]'
    Matches_count = '//*[text()="Matches count"]'
    Players_count = '//*[text()="Players count"]'
    Button_Players = '//*[text()="Players"]'
    last_created_player = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/h6[1]'
    sign_out_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.activity_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_a_player(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def wait(self):
        self.wait_for_element_to_be_clickable(self.activity_xpath)
        time.sleep(4)
