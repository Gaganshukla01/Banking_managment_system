import pytest
from unittest.mock import patch
from view.user_sign_up import SignupBankAccount

class TestAuth:

    def setup_method(self):

        self.sign_up = SignupBankAccount()

    @patch('builtins.input', side_effect=['Prince Shukla', "34", 'address', 'p@yash.com', '8349061831', 'xsw2XSW@', 'xsw2XSW@'])
    def test_signup(self, mock_input):

        res = self.sign_up.signup_bank_account()
        assert res is True
    