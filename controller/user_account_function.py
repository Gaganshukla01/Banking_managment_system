from view.bank_services import(credit_amount,debit_amount,show_balance,transfer_money)

def account_operation(user_account_number):

    """
    Manages account operations for a user in the Bank Management System.

    This function provides a command-line interface for users to perform various operations 
    on their bank account, including debiting an amount, crediting an amount, and checking 
    the account balance. It continuously prompts the user for their choice until they decide 
    to exit the operation menu.

    The available operations are:
    - Press 1 to debit an amount from the account.
    - Press 2 to credit an amount to the account.
    - Press 3 to show the current balance of the account.
    - Press any other key to exit the operation menu.

    The function calls the `debit_amount`, `credit_amount`, and `show_balance` functions 
    based on the user's input. If the user chooses to exit, the loop terminates.

    Parameters:
        user_account_number (str): The account number of the user whose operations are being managed.

    Returns:
        None
    """

    while True:
        print("-------------------------------------------------------||")
        print("Press 1 for debit from account: ")
        print("-------------------------------------------------------||")
        print("Press 2 for credit from account: ")
        print("-------------------------------------------------------||")
        print("Press 3 for show balance: ")
        print("-------------------------------------------------------||")
        print("Press 4 for transfer money via account number : ")
        print("-------------------------------------------------------||")
        print("Press any key for exit with bank account: ")
        print("-------------------------------------------------------||")
        user_choice=input("Enter your choice: ")
        if user_choice=="1":
            debit_amount(user_account_number)
        elif user_choice=="2":
            credit_amount(user_account_number)
        elif user_choice=="3":
            show_balance(user_account_number)
        elif user_choice=="4":
            transfer_money(user_account_number)
        else:
            break
