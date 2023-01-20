from pages.base_page import BasePage


class Dashboard(BasePage):
    Clear_button = '//*[text()="Clear"]'
    Submit_button = '//*[text()="Submit"]'
    Match_at_home_box = '//*[text()="Match at home"]'
    Match_out_home_box = '//*[text()="Match out home"]'
    Main_page_button = '//child::div[1]/div[2]'
    Date_field = '//child::div[1]/div[5]/div/div'
    Enemy_team_score = '//child::div[1]/div[4]'
    Match_boxes_zone = '//child::div[1]/div[6]'
    Time_played_field = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input'
    Rating = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input'
    Reports_Button = '//*[text()="Reports"]'
    Players_button = '//*[text()="Players"]'
    Matches_Button = '//*[text()="Matches"]'

pass
