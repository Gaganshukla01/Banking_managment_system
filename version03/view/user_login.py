from colorama import (Fore, Style)
from model.bank_user_ import UserData
from controller.user_account_function import AccountOperation

class LoginBankAccount:
    
    def __init__(self):

        self.operation=AccountOperation()
        self.user_data=UserData()

    def login_bank_account(self):
    
        while True:
            
            try:
                print(Fore.BLUE + "Welcome To Login Page...| " + Style.RESET_ALL)
                print("----------------------------------------------------------||")
                user_account_number = input(Fore.MAGENTA + "Enter user account number: "
                                                                     + Style.RESET_ALL)
                print("----------------------------------------------------------||")
                user_password = input(Fore.MAGENTA + "Enter your password: " + Style.RESET_ALL)
                print("----------------------------------------------------------||")
                data=self.user_data.display()
                for index in data:
                    if user_account_number and user_password in index:
                        print(f"Welcome {index[1]}")
                        print(Fore.GREEN+f"Login sucessfully with account number {user_account_number}")
                        self.operation.account_operation(user_account_number)
                else:
                     print(Fore.RED+f"Acoount not found")
                
            except FileNotFoundError:
                print("Error: The data file was not found. Please check the file path.")
                break  
        
            except KeyError as e:
                print(f"Error: Missing expected data in the file. {e}")
                break  
        
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break   
