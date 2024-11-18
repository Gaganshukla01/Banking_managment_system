from model.bank_user_ import UserData
from model.transaction import TransactionData
user_data = UserData("./model/data.json")
transaction_data=TransactionData("./model/transaction_data.json")

def show_balance(user_account_number):

    """
    Displays the current balance of the specified user account.

    This function retrieves the balance for the given account number from the user data 
    and prints it to the console.

    Parameters:
        user_account_number (str): The account number of the user whose balance is to be displayed.

    Returns:
        None: This function does not return a value; it prints the account balance directly.
    
    Raises:
        KeyError: If the account number does not exist in the user data.
    """

    data=user_data.display()
    user_amount=data[user_account_number]["Balance"]
    print(f"Account balance is {user_amount}")
    
def credit_amount(user_account_number):

    """
    Credits a specified amount to the user's account.

    This function prompts the user to enter an amount to credit to their account, 
    updates the account balance, and prints the new balance.

    Parameters:
        user_account_number (str): The account number of the user to credit the amount to.

    Returns:
        None: This function does not return a value; it prints the success message and updated balance directly.
    
    Raises:
        ValueError: If the input amount is not a valid integer.
        KeyError: If the account number does not exist in the user data.
    """

    data=user_data.display()
    mode="credit"
    user_amount_input=int(input("Enter amount you want to credit: "))
    updated_amount=data[user_account_number]["Balance"]+user_amount_input
    user_data.update_balance(user_account_number,updated_amount)
    print(f"{user_amount_input} credited successfully ")
    print(f"Available balance is {updated_amount}")
    # for adding transaction details
    transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount)
    
def debit_amount(user_account_number):

    """
    Debits a specified amount from the user's account.

    This function prompts the user to enter an amount to debit from their account, 
    checks for sufficient balance, and updates the account balance accordingly.

    Parameters:
        user_account_number (str): The account number of the user to debit the amount from.

    Returns:
        None: This function does not return a value; it prints the success message, 
              available balance, or error messages directly.
    
    Raises:
        ValueError: If the input amount is not a valid integer.
        KeyError: If the account number does not exist in the user data.
    """

    try:

        user_amount_input = int(input("Enter amount you want to debit: "))
        if user_amount_input < 0:
            print("You cannot debit a negative amount.")
            return
        data=user_data.display()
        current_amount=data[user_account_number]["Balance"]
        print(current_amount)
        if current_amount < user_amount_input:
            print("Insufficient balance.")
        elif current_amount == user_amount_input:
            print("You cannot empty your bank account.")
        else:
            mode="debit"
            updated_amount=current_amount - user_amount_input
            user_data.update_balance(user_account_number, updated_amount)
            print(f"{user_amount_input} debited successfully.")
            print(f"Available balance is {updated_amount}.")
            # for adding debit details
            transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount)
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyError:
        print(f"Account number {user_account_number} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Thanks for using the bank.")

def transfer_money(user_account_number):

    transfer_account_number=input("Enter account number in which you want to send money: ")
    amount=int(input("Enter amount you want to send: "))
    data=user_data.display()
    account_number=list(data.keys())
    current_amount=int(data[user_account_number]['Balance'])
    if amount>current_amount:
        print("Insufficent balance in your account")
        return
    if transfer_account_number in account_number:
        updated_balance=int(data[transfer_account_number]['Balance'])+amount
        user_data.update_balance(transfer_account_number,updated_balance)
        print(f"Amount transfer sucessfully to {transfer_account_number} ")
        updated_amount=data[user_account_number]["Balance"]-amount
        user_data.update_balance(user_account_number,updated_amount)
        # for saving transaction for sender
        transaction_data.save_transaction(user_account_number,"Transfer",amount,updated_amount)
        # for saving transaction for reciver
        tranfer_update_balance=data[transfer_account_number]['Balance']+amount
        transaction_data.save_transaction(transfer_account_number,"Recived",amount,
                                            tranfer_update_balance)
    else:
        print(f"{transfer_account_number} does not exist")
        return
        