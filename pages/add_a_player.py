import time
from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath = '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[2]'
    expected_title = "Add player"
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def click_on_the_add_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page( self ):
        time.sleep(5)
        actual_title = self.get_page_title(self.add_a_player_url)
        print(f"Actual title: {actual_title}")
        print(f"Expected title: {self.expected_title}")
        assert actual_title == self.expected_title





