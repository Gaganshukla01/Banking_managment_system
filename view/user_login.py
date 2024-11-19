from colorama import (Fore, Style)
from model.bank_user_ import UserData
from controller.user_account_function import account_operation

# decorator creation
def login_required(func):

    def inner(res):

        print(f"Login result: {'Success' if res else 'Failure'}")
        return res  

    return inner  

@login_required
def check(res):
    
    return res  

def login_bank_account():
    
    result = None  
    while True:
        try:
            print(Fore.BLUE + "Welcome To Login Page...| " + Style.RESET_ALL)
            print("----------------------------------------------------------||")
            user_account_number = input(Fore.MAGENTA + "Enter user account number: " + Style.RESET_ALL)
            print("----------------------------------------------------------||")
            user_password = input(Fore.MAGENTA + "Enter your password: " + Style.RESET_ALL)
            print("----------------------------------------------------------||")
            user_data = UserData("./model/data.json")
            data = user_data.display()
            user_account_keys = list(data.keys())
            
            if (user_account_number in user_account_keys and 
                data[user_account_number]["Password"] == user_password):
                print(Fore.GREEN + f"Welcome {data[user_account_number]['Name']}" + Style.RESET_ALL)
                print(f"Login successful with account number: {user_account_number}")
                res=True
                result=check(res)  
                break  
            else:
                print(Fore.RED + "Invalid account number or password. Please try again.")
                res=False 
                result=check(res)  
            
            print(f"Check function returned: {result}")  
            
        except FileNotFoundError:
            print("Error: The data file was not found. Please check the file path.")
            break  
        
        except KeyError as e:
            print(f"Error: Missing expected data in the file. {e}")
            break  
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  

    return result ,user_account_number 
