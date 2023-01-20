from pages.base_page import BasePage


class Dashboard(BasePage):
    button_Main_Page = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    Reports_count = '//*[text()="Reports count"]'
    Shortcuts = '//*[text()="Shortcuts"]'
    Activity = '//*[text()="Activity"]'
    Events_count = '//*[text()="Events count"]'
    Matches_count = '//*[text()="Matches count"]'
    Players_count = '//*[text()="Players count"]'
    Button_Players = '//*[text()="Players"]'
    button_language_Polski = '//*[text()="Polski"]'
    button_dev_team_contact = '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]'
    button_sing_out = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]'
pass