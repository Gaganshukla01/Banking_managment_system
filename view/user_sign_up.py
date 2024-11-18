from model.bank_user_ import UserData
from service.account_number_genrate import user_account_number_genrate
from service.user_validation import (
    name_valid, age_valid,
    address_valid, email_valid, 
    phone_valid, password_valid
)

def get_valid_input(prompt, validation_func):

    while True:
        user_input = input(prompt)
        is_valid, message = validation_func(user_input)
        if is_valid:
            return user_input
        else:
            print(message)  

def signup_bank_account():
    
    """
    Handles the signup process for creating a new bank account.

    This function collects user information such as name, age, address, email, phone number, 
    and password. It validates the inputs using predefined validation functions. If all inputs 
    are valid, it generates a new account number, initializes the account balance, and saves 
    the user data to a JSON file.

    The function performs the following steps:
    1. Prompts the user for their name, age, address, email, and phone number, validating each input.
    2. Asks the user to enter and confirm their password, ensuring both entries match.
    3. Generates a unique account number for the new user.
    4. Initializes the account balance to zero.
    5. Saves the user data to a JSON file using the `User Data` class.

    Returns:
        None: This function does not return a value; it prints messages indicating the success 
              or failure of the signup process.

    Raises:
        Exception: For any unexpected errors that may occur during execution, such as issues 
                   with file handling or data insertion.
    """
    
    try:
        user_name = get_valid_input("Enter your name: ", name_valid)
        user_age = get_valid_input("Enter your age: ", age_valid)
        user_address = get_valid_input("Enter your address: ", address_valid)
        user_email = get_valid_input("Enter your email: ", email_valid)
        user_phone_number = get_valid_input("Enter your phone number: ", phone_valid)
        
        while True:
            user_password = input("Enter password: ")
            user_confirm_password = input("Confirm password: ")
            if user_password == user_confirm_password:
                break
            else:
                print("Check password and confirm password")

        # If all inputs are valid...
        user_data = UserData("./model/data.json")
        user_account_number = user_account_number_genrate()
        user_account_balance=0
        print(f"Account created successfully with account number {user_account_number}")
        user_data.insert(user_name, user_age, user_address, user_email, user_phone_number, 
                         user_password, user_account_number,user_account_balance)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Signup process completed.")  
