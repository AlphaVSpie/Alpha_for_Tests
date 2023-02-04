import time
from pages.base_page import BasePage

class RemindPassword(BasePage):
    email_field_xpath = '//*[@id="__next"]/div[1]/div/div[1]/div/div/input'
    send_button_xpath = '//*[@id="__next"]/div[1]/div/div[2]/button/span'
    message_sent_box_xpath = '//*[@id="__next"]/div[2]/div'
    remind_password_url = 'https://scouts-test.futbolkolektyw.pl/en/remind'
    expected_title = 'Remind password'

    def title_of_page( self ):
        time.sleep(5)
        actual_title = self.get_page_title(self.remind_password_url)
        print(f"Actual title: {actual_title}")
        print(f"Expected title: {self.expected_title}")
        assert actual_title == self.expected_title

    def message_sent( self ):
        self.visibility_of_element_located(self.message_sent_box_xpath)

    def click_send( self ):
        self.click_on_the_element(self.send_button_xpath)

    def type_in_email( self, email ):
        self.field_send_keys(self.email_field_xpath, email)


