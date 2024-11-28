import pytest
from unittest.mock import patch
from view.bank_services import Operation

class TestBanking:

    def setup_method(self, method):
        
        self.bank_operation = Operation()
        print("Method called:")
 
    # credit test case
    @patch('builtins.input', side_effect=['500'])  
    def test_credit(self, mock_input):
        
        result = self.bank_operation.credit_amount(2400)  
        assert result is True  

    @patch('builtins.input',side_effect=['-600'])
    def test_credit(self,mock_input):

        result=self.bank_operation.credit_amount(2400)
        assert result is False

    # debit test cases
    @patch('builtins.input',side_effect=['-600'])
    def test_debit(self,mock_input):

        result=self.bank_operation.debit_amount(2400)
        assert result is False
    
    @patch('builtins.input',side_effect=['5000000000'])
    def test_debit(self,mock_input):

        result=self.bank_operation.debit_amount(2400)
        assert result is False
    
    @patch('builtins.input',side_effect=['600'])
    def test_debit(self,mock_input):

        result=self.bank_operation.debit_amount('2401')
        assert result is True
    
    # trasfer test case
    @patch('builtins.input',side_effect=['5000000000'])
    def test_transfer(self,mock_input):

        result=self.bank_operation.transfer_money('2400')
        assert result is False
    
    @patch('builtins.input',side_effect=['-500'])
    def test_transfer(self,mock_input):

        result=self.bank_operation.transfer_money(2400)
        assert result is None
      