import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    add_player_button_xpath = "//span[normalize-space()='Add player']"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'

    def title_of_page( self ):
        time.sleep(5)
        actual_title = self.get_page_title(self.dashboard_url)
        print(f"Actual title: {actual_title}")
        print(f"Expected title: {self.expected_title}")
        assert actual_title == self.expected_title

    def click_add_a_player( self ):
        self.click_on_the_element(self.add_player_button_xpath)

