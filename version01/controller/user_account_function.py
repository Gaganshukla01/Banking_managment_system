from colorama import (Fore,Style)
from constant.constant import(DEBIT_AMOUNT,CREDIT_AMOUNT,SHOW_BALANCE,TRANSFER_MONEY)
from view.bank_services import(credit_amount,debit_amount,show_balance,transfer_money)

def account_operation(user_account_number):

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
        print(Fore.YELLOW+"Press any key for exit with bank account: "+Style.RESET_ALL)
        print("-------------------------------------------------------||")

        user_choice=int(input(Fore.BLUE+"Enter your choice: "+Style.RESET_ALL))
        
        if user_choice==DEBIT_AMOUNT:
            debit_amount(user_account_number)
        elif user_choice==CREDIT_AMOUNT:
            credit_amount(user_account_number)
        elif user_choice==SHOW_BALANCE:
            show_balance(user_account_number)
        elif user_choice==TRANSFER_MONEY:
            transfer_money(user_account_number)
        else:
            break
