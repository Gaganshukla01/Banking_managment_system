from view.user_login import  login_bank_account
from view.user_sign_up import signup_bank_account
from constant.constant import(SIGNUP_ACCOUNT,LOGIN_ACCOUNT)

def bank_controller():

    """
    Manages the user interaction for the Bank Management System.

    This function provides a command-line interface for users to either sign up for a new bank account 
    or log in to an existing account. It continuously prompts the user for their choice until they 
    decide to exit the system.

    The available options are:
    - Press 1 to sign up for a new bank account.
    - Press 2 to log in to an existing bank account.
    - Press any other key to exit the system.

    The function calls the `signup_bank_account` function when the user chooses to sign up, 
    and the `login_bank_account` function when the user chooses to log in. If the user chooses 
    to exit, a thank you message is displayed, and the loop terminates.

    Returns:
        None
    """

    while True:
        print(" WELCOME TO BANK MANAGMENT SYSTEM ")
        print("-------------------------------------------------------||")
        print("Press 1 for signup with bank account: ")
        print("-------------------------------------------------------||")
        print("Press 2 for login with bank account: ")
        print("-------------------------------------------------------||")
        print("Press any key for exit with bank account: ")
        print("-------------------------------------------------------||")
        user_choice=input("Enter your choice:. ")
        if user_choice=="1":
            signup_bank_account()
        elif user_choice=="2":
            login_bank_account()
        else:
            print("Thanks for using bank system........")
            break 
