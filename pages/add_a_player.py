import time
from pages.base_page import BasePage


class AddPlayer(BasePage):
    expected_title = "Add player"
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_language_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]'
    languages_box_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[''15]/div/div/div/input'
    languages_box_title = 'Languages'
    main_page_button_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    email_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input'
    name_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input'
    surname_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input'
    phone_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input'
    weight_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input'
    height_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input'
    age_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input'
    leg_field_xpath = '//*[@id="mui-component-select-leg"]'
    right_leg_xpath = '//*[@id="menu-leg"]/div[3]/ul/li[1]'
    club_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input'
    level_field_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input'
    main_position_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input'
    district_field_xpath = '//*[@id="mui-component-select-district"]'
    opole_xpath = '//*[@id="menu-district"]/div[3]/ul/li[8]'
    submit_button_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]'
    human_xpath = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[1]/svg'
    confirmation_xpath = '//*[@id="__next"]/div[2]/div'
    required_surname_xpath = '//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/p'


    def title_of_page( self ):
        time.sleep(5)
        actual_title = self.get_page_title(self.add_a_player_url)
        print(f"Actual title: {actual_title}")
        print(f"Expected title: {self.expected_title}")
        assert actual_title == self.expected_title

    def click_add_language( self ):
        self.click_on_the_element(self.add_language_xpath)

    def visibility( self ):
        self.visibility_of_element_located(self.languages_box_xpath)

    def type_in_languages( self, languages ):
        self.field_send_keys(self.languages_box_xpath, languages)

    def click_main_page( self ):
        self.click_on_the_element(self.main_page_button_xpath)

    def type_in_e_mail( self, e_mail ):
        self.field_send_keys(self.email_field_xpath, e_mail)

    def type_in_name( self, name ):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname( self, surname ):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone( self, phone ):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight( self, weight ):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height( self, height ):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age( self, age ):
        self.field_send_keys(self.age_field_xpath, age)

    def click_leg( self ):
        self.click_on_the_element(self.leg_field_xpath)

    def click_right_leg( self ):
        self.click_on_the_element(self.right_leg_xpath)

    def type_in_club( self, club ):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level( self, level ):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_main_position( self, position ):
        self.field_send_keys(self.main_position_xpath, position)

    def click_district( self ):
        self.click_on_the_element(self.district_field_xpath)

    def click_opole( self ):
        self.click_on_the_element(self.opole_xpath)

    def click_submit( self ):
        self.click_on_the_element(self.submit_button_xpath)

    def conf( self ):
        self.visibility_of_element_located(self.confirmation_xpath)

    def click_surname( self ):
        self.click_on_the_element(self.surname_field_xpath)


