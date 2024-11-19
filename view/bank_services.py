from colorama import (Fore,Style)
from model.bank_user_ import UserData
from model.transaction import TransactionData
from constant.constant import(WITHDRAW_LIMIT,TRANSFER_LIMIT)
user_data = UserData("./model/data.json")
transaction_data=TransactionData("./model/transaction_data.json")

def show_balance(user_account_number):

    data=user_data.display()
    user_amount=data[user_account_number]["Balance"]
    print(Fore.GREEN+f"Account balance is {user_amount}"+Style.RESET_ALL)
    
def credit_amount(user_account_number):

    data=user_data.display()
    mode="credit"
    user_amount_input=int(input("Enter amount you want to credit: "))
    updated_amount=data[user_account_number]["Balance"]+user_amount_input
    user_data.update_balance(user_account_number,updated_amount)
    print(Fore.GREEN+f"{user_amount_input} credited successfully "+Style.RESET_ALL)
    print(Fore.GREEN+f"Available balance is {updated_amount}"+Style.RESET_ALL)
    # for adding transaction details
    transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount)
    
def debit_amount(user_account_number):

    try:
        user_amount_input = int(input("Enter amount you want to debit: "))
        if user_amount_input < 0:
            print(Fore.RED+"You cannot debit a negative amount."+Style.RESET_ALL)
            return
        if user_amount_input>WITHDRAW_LIMIT:
            print(Fore.RED+"Limit reached"+Style.RESET_ALL)
            return
        data=user_data.display()
        current_amount=data[user_account_number]["Balance"]
        print(current_amount)
        if current_amount < user_amount_input:
            print(Fore.RED+"Insufficient balance."+Style.RESET_ALL)
        elif current_amount == user_amount_input:
            print(Fore.YELLOW+"You cannot empty your bank account."+Style.RESET_ALL)
        else:
            mode="debit"
            updated_amount=current_amount - user_amount_input
            user_data.update_balance(user_account_number, updated_amount)
            print(Fore.GREEN+f"{user_amount_input} debited successfully."+Style.RESET_ALL)
            print(Fore.GREEN+f"Available balance is {updated_amount}."+Style.RESET_ALL)
            # for adding debit details
            transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount)
    
    except ValueError:
        print(Fore.RED+"Invalid input. Please enter a valid number."+Style.RESET_ALL)
    except KeyError:
        print(Fore.RED+f"Account number {user_account_number} does not exist."+Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+f"An unexpected error occurred: {e}"+Style.RESET_ALL)

    print(Fore.BLUE+"Thanks for using the bank."+Style.RESET_ALL)

def transfer_money(user_account_number):

    transfer_account_number=input("Enter account number in which you want to send money: ")
    amount=int(input(Fore.YELLOW+"Enter amount you want to send: "+Style.RESET_ALL))
    data=user_data.display()
    account_number=list(data.keys())
    current_amount=int(data[user_account_number]['Balance'])
    if amount>current_amount:
        print(Fore.RED+"Insufficent balance in your account"+Style.RESET_ALL)
        return
    if user_amount_input>TRANSFER_LIMIT:
            print(Fore.RED+"Limit reached"+Style.RESET_ALL)
            return
    if transfer_account_number in account_number:
        updated_balance=int(data[transfer_account_number]['Balance'])+amount
        user_data.update_balance(transfer_account_number,updated_balance)
        print(Fore.GREEN+f"Amount transfer sucessfully to {transfer_account_number} "+Style.RESET_ALL)
        updated_amount=data[user_account_number]["Balance"]-amount
        user_data.update_balance(user_account_number,updated_amount)
        # for saving transaction for sender
        transaction_data.save_transaction(user_account_number,"Transfer",
                                            amount,updated_amount,True,transfer_account_number)
        # for saving transaction for reciver
        tranfer_update_balance=data[transfer_account_number]['Balance']+amount
        transaction_data.save_transaction(transfer_account_number,"Recived",amount,
                                            tranfer_update_balance,False,user_account_number)
    else:
        print(Fore.RED+f"{transfer_account_number} does not exist"+Style.RESET_ALL)
        return
        