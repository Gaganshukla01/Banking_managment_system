from colorama import (Fore,Style)
from controller.auth_controller import banking_auth
from view.user_login import  (login_bank_account,check)
from view.user_sign_up import signup_bank_account
from constant.constant import(SIGNUP_ACCOUNT,LOGIN_ACCOUNT,BANKING)

def bank_controller():

    """
    This function provides a command-line interface for users to either sign up for a new bank account 
    or log in to an existing account. It continuously prompts the user for their choice until they 
    decide to exit the system.
    """
    user_account_number=None
    check_response=False

    while True:

        print(Fore.BLUE+"WELCOME TO BANK MANAGMENT SYSTEM "+Style.RESET_ALL)
        print("-------------------------------------------------------||")
        print(Fore.YELLOW+"Press 1 for signup with bank account: "+Style.RESET_ALL)
        print(Fore.YELLOW+"-------------------------------------------------------||"+Style.RESET_ALL)
        print(Fore.YELLOW+"Press 2 for login with bank account: "+Style.RESET_ALL)
        print(Fore.YELLOW+"-------------------------------------------------------||"+Style.RESET_ALL)
        print(Fore.YELLOW+"Press 3 for banking with bank account: "+Style.RESET_ALL)
        print(Fore.YELLOW+"-------------------------------------------------------||"+Style.RESET_ALL)
        print(Fore.YELLOW+"Press any key for exit with bank account: "+Style.RESET_ALL)
        print(Fore.YELLOW+"-------------------------------------------------------||"+Style.RESET_ALL)

        user_choice=int(input("Enter your choice:. "))
        if user_choice==SIGNUP_ACCOUNT:
            signup_bank_account()
        elif user_choice==LOGIN_ACCOUNT:
            check_response,user_account_number=login_bank_account()
        elif user_choice==BANKING:
            if check_response:
                banking_auth(user_account_number)
                check_response=False
            else:
                print("You are not logged in yet")
        else:
            print("Thanks for using bank system........")
            break 
