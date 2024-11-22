import pytest
from unittest.mock import patch
from view.bank_services import Operation

class TestBanking:
    def setup_method(self, method):
        self.bank_operation = Operation()
        print("Method called:")

    @patch('builtins.input', side_effect=['500'])  
    def test_credit(self, mock_input):
        
        result = self.bank_operation.credit_amount(12345)  
        assert result is True  
            