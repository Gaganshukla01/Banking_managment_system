from colorama import (Fore,Style)
from view.user_login import LoginBankAccount
from view.user_sign_up import SignupBankAccount
from constant.constant import(SIGNUP_ACCOUNT,LOGIN_ACCOUNT,BANKING)

class BankController:

    def __init__(self):
        self.sign_up=SignupBankAccount()
        self.login=LoginBankAccount()

    def bank_controller(self):

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
            print(Fore.YELLOW+"-------------------------------------------------------||"
                        +Style.RESET_ALL)
            print(Fore.YELLOW+"Press 2 for login with bank account: "+Style.RESET_ALL)
            print(Fore.YELLOW+"-------------------------------------------------------||"
                        +Style.RESET_ALL)
            print(Fore.YELLOW+"Press 3 for banking with bank account: "+Style.RESET_ALL)
            print(Fore.YELLOW+"-------------------------------------------------------||"
                        +Style.RESET_ALL)
            print(Fore.YELLOW+"Press any key for exit with bank account: "+Style.RESET_ALL)
            print(Fore.YELLOW+"-------------------------------------------------------||"
                        +Style.RESET_ALL)

            user_choice=int(input("Enter your choice:. "))
            if user_choice==SIGNUP_ACCOUNT:
                self.sign_up.signup_bank_account()
            elif user_choice==LOGIN_ACCOUNT:
                self.login.login_bank_account()
            elif user_choice==BANKING:
                if check_response:
                    self.auth.banking_auth(user_account_number)
                    check_response=False
                else:
                    print("You are not logged in yet")
            else:
                print("Thanks for using bank system........")
                break 
