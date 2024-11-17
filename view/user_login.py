from model.bank_user_ import UserData
from controller.user_account_function import account_operation

def login_bank_account():

    """
    Handles the login process for a bank account.

    This function prompts the user to enter their account number and password. 
    It validates the credentials against the stored user data. If the login is successful, 
    it welcomes the user and initiates account operations. If the login fails, it prompts 
    the user to try again.

    The function performs the following steps:
    1. Continuously prompts the user for their account number and password until a successful login occurs or an error is encountered.
    2. Loads user data from a JSON file using the `User Data` class.
    3. Checks if the provided account number exists and if the password matches the stored password.
    4. If the login is successful, it prints a welcome message and calls the `account_operation` function with the user's account number.
    5. If the login fails, it informs the user and allows them to retry.

    Returns:
        None: This function does not return a value; it either initiates account operations or prints error messages.

    Raises:
        FileNotFoundError: If the data file cannot be found.
        KeyError: If the expected data is missing in the user data.
        Exception: For any other unexpected errors that may occur during execution.
    """

    while True:
        try:
            print("Welcome To Login Page...| ")
            print("----------------------------------------------------------||")
            user_account_number = input("Enter user account number: ")
            print("----------------------------------------------------------||")
            user_password = input("Enter your password: ")
            print("----------------------------------------------------------||")
            user_data = UserData("./model/data.json")
            data = user_data.display()
            user_account_keys = list(data.keys())
            
            if (user_account_number in user_account_keys and 
                data[user_account_number]["Password"] == user_password):
                print(f"Welcome {data[user_account_number]["Name"]}")
                print(f"Login successfull with account number:{user_account_number}")
                account_operation(user_account_number)
                break
            else:
                print("Invalid account number or password. Please try again.")
        
        except FileNotFoundError:
            print("Error: The data file was not found. Please check the file path.")
            break  
        
        except KeyError as e:
            print(f"Error: Missing expected data in the file. {e}")
            break  
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  
        