import time
from pages.base_page import BasePage


class AddPlayer(BasePage):
    expected_title = "Add player"
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

    def title_of_page( self ):
        time.sleep(5)
        actual_title = self.get_page_title(self.add_a_player_url)
        print(f"Actual title: {actual_title}")
        print(f"Expected title: {self.expected_title}")
        assert actual_title == self.expected_title





