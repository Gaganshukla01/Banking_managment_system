from colorama import (Fore,Style)
from model.bank_user_ import UserData
from model.transaction import TransactionData
from constant.constant import(WITHDRAW_LIMIT,TRANSFER_LIMIT)

class Operation:

    def __init__(self):

        self.user_data = UserData()
        self.transaction_data=TransactionData("./model/transaction_data.json")

    def show_balance(self,user_account_number):

        data=self.user_data.display()
        user_amount=0
        for index in data:
            if index[0]==user_account_number:
                user_amount=index[-1]
                break
        print(Fore.GREEN+f"Account balance is {user_amount}"+Style.RESET_ALL)
    
    def credit_amount(self,user_account_number):

        data=self.user_data.display()
        mode="credit"
        user_amount_input=int(input("Enter amount you want to credit: "))
        for index in data:
            if index[0]==user_account_number:
                updated_amount=index[-1]+user_amount_input
        self.user_data.update_balance(user_account_number,updated_amount)
        print(Fore.GREEN+f"{user_amount_input} credited successfully "+Style.RESET_ALL)
        print(Fore.GREEN+f"Available balance is {updated_amount}"+Style.RESET_ALL)
        # for adding transaction details
        self.transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount,3,"NA")
    
    def debit_amount(self,user_account_number):

        try:
            user_amount_input = int(input("Enter amount you want to debit: "))
            if user_amount_input < 0:
                print(Fore.RED+"You cannot debit a negative amount."+Style.RESET_ALL)
                return
            if user_amount_input>WITHDRAW_LIMIT:
                print(Fore.RED+"Limit reached"+Style.RESET_ALL)
                return
            data=self.user_data.display()
            for index in data:
                if index[0]==user_account_number:
                    current_amount=index[-1]
            print(current_amount)
            if current_amount < user_amount_input:
                print(Fore.RED+"Insufficient balance."+Style.RESET_ALL)
            elif current_amount == user_amount_input:
                print(Fore.YELLOW+"You cannot empty your bank account."+Style.RESET_ALL)
            else:
                mode="debit"
                updated_amount=current_amount - user_amount_input
                self.user_data.update_balance(user_account_number, updated_amount)
                print(Fore.GREEN+f"{user_amount_input} debited successfully."+Style.RESET_ALL)
                print(Fore.GREEN+f"Available balance is {updated_amount}."+Style.RESET_ALL)
                # for adding debit details
                # self.transaction_data.save_transaction(user_account_number,mode,user_amount_input,updated_amount,3,"NA")
    
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a valid number."+Style.RESET_ALL)
        except KeyError:
            print(Fore.RED+f"Account number {user_account_number} does not exist."+Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED+f"An unexpected error occurred: {e}"+Style.RESET_ALL)
        print(Fore.BLUE+"Thanks for using the bank."+Style.RESET_ALL)

    def transfer_money(self, user_account_number):

        try:
            transfer_account_number = input("Enter account number in which you want to send money: ")
            amount = int(input(Fore.YELLOW + "Enter amount you want to send: " + Style.RESET_ALL))
            data = self.user_data.display()
            current_amount = 0
            transfer_account_exists = False
            # Check if the user account number exists and get the current balance
            for index in data:
                if index[0] == user_account_number:
                    current_amount = index[-1]
                if index[0] == transfer_account_number:
                    transfer_account_exists = True
            if not transfer_account_exists:
                print(Fore.RED + f"{transfer_account_number} does not exist." + Style.RESET_ALL)
                return

            # Check if the user has sufficient balance and if the amount is within the transfer limit
            if amount > current_amount:
                print(Fore.RED + "Insufficient balance in your account." + Style.RESET_ALL)
                return
            if amount > TRANSFER_LIMIT:
                print(Fore.RED + "Transfer limit reached." + Style.RESET_ALL)
                return
            # Update balances
            updated_sender_balance = current_amount - amount
            self.user_data.update_balance(user_account_number, updated_sender_balance)
            # Update receiver's balance
            for index in data:
                if index[0] == transfer_account_number:
                    updated_receiver_balance = index[-1] + amount
                    self.user_data.update_balance(transfer_account_number, updated_receiver_balance)
                    break

            print(Fore.GREEN + f"Amount transferred successfully to {transfer_account_number}." + Style.RESET_ALL)

        # # For saving transaction for sender
        # self.transaction_data.save_transaction(user_account_number, "Transfer", amount, updated_sender_balance, True, transfer_account_number)

        # # For saving transaction for receiver
        # self.transaction_data.save_transaction(transfer_account_number, "Received", amount, updated_receiver_balance, False, user_account_number)

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
        except KeyError:
            print(Fore.RED + f"Account number {user_account_number} does not exist." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}" + Style.RESET_ALL)
        



 # for saving transaction for sender
            # self.transaction_data.save_transaction(user_account_number,"Transfer",
            #                                 amount,updated_amount,True,transfer_account_number)
            # # for saving transaction for reciver
            # tranfer_update_balance=data[transfer_account_number]['Balance']+amount
            # self.transaction_data.save_transaction(transfer_account_number,"Recived",amount,
            #                                 tranfer_update_balance,False,user_account_number)