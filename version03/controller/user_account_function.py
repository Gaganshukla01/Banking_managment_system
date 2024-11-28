from colorama import (Fore,Style)
from view.bank_services import Operation
from constant.constant import(DEBIT_AMOUNT,CREDIT_AMOUNT,SHOW_BALANCE,
                                TRANSFER_MONEY,SHOW_ACCOUNT,TRANSACTION_HISTORY)

class AccountOperation:

    def __init__(self):

        self.bank=Operation()

    def account_operation(self,user_account_number):

        """
        The function calls the `debit_amount`, `credit_amount`, and `show_balance` functions 
        based on the user's input. If the user chooses to exit, the loop terminates.
        """

        while True:
            
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 1 for debit from account: "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 2 for credit from account: "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 3 for show balance: "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 4 for transfer money via account number : "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 5 for show transaction history : "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press 6 for show account details : "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            print(Fore.YELLOW+"Press any key for exit with bank account: "+Style.RESET_ALL)
            print("-------------------------------------------------------||")
            user_choice=int(input(Fore.BLUE+"Enter your choice: "+Style.RESET_ALL))
            if user_choice==DEBIT_AMOUNT:
                self.bank.debit_amount(user_account_number)
            elif user_choice==CREDIT_AMOUNT:
                self.bank.credit_amount(user_account_number)
            elif user_choice==SHOW_BALANCE:
                self.bank.show_balance(user_account_number)
            elif user_choice==TRANSFER_MONEY:
                self.bank.transfer_money(user_account_number)
            elif user_choice==TRANSACTION_HISTORY:
                self.bank.transaction_history(user_account_number)
            elif user_choice==SHOW_ACCOUNT:
                self.bank.show_account(user_account_number)
            else:
                return
                