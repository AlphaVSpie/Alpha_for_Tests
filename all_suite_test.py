import unittest

from unittest.loader import makeSuite

from test_cases.framework import Test
from test_cases.login_to_the_system import TestLoginPage
from test_cases.empty_required_field_test import TestEmptyField
from test_cases.remind_password_test import TestRemindPassword
from test_cases.returt_to_main_page_test import TestReturnMainPage
from test_cases.add_player_test import TestAddPlayer
from test_cases.add_language_button import TestAddLanguageButton
from test_cases.new_player_creating import TestNewPlayerCreating
from test_cases.sing_out import TestSingOut
from test_cases.negative_login_to_the_system import TestLoginPageNegative


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(Test))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestEmptyField))
    test_suite.addTest(makeSuite(TestRemindPassword))
    test_suite.addTest(makeSuite(TestReturnMainPage))
    test_suite.addTest(makeSuite(TestAddPlayer))
    test_suite.addTest(makeSuite(TestAddLanguageButton))
    test_suite.addTest(makeSuite(TestNewPlayerCreating))
    test_suite.addTest(makeSuite(TestSingOut))
    test_suite.addTest(makeSuite(TestLoginPageNegative))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
