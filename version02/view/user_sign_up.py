from model.bank_user_ import UserData
from service.user_validation import Validation
from service.account_number_genrate import AccountNumberGenerator

class SignupBankAccount:

    def __init__ (self):
        self.user_data = UserData("./model/data.json")
        self.genrate=AccountNumberGenerator()
    
    def get_valid_input(self,prompt, validation_func):

        while True:
            user_input = input(prompt)
            is_valid, message = validation_func(user_input)
            if is_valid:
                return user_input
            else:
                print(message)  

    def signup_bank_account(self):
    
        """
        This function collects user information such as name, age, address, email, phone number, 
        and password. It validates the inputs using predefined validation functions. If all inputs 
        are valid, it generates a new account number, initializes the account balance, and saves 
        the user data to a JSON file.
        """
    
        try:
            user_name=self.get_valid_input("Enter your name: ", Validation.name_valid)
            user_age=self.get_valid_input("Enter your age: ", Validation.age_valid)
            user_address=self.get_valid_input("Enter your address: ", Validation.address_valid)
            user_email=self.get_valid_input("Enter your email: ", Validation.email_valid)
            user_phone_number=self.get_valid_input("Enter your phone number: ", Validation.phone_valid)
        
            while True:
                user_password = input("Enter password: ")
                user_confirm_password = input("Confirm password: ")
                if user_password == user_confirm_password:
                    break
                else:
                    print("Check password and confirm password")

            # If all inputs are valid...
            user_account_number = self.genrate.user_account_number_generate()
            user_account_balance=0
            print(f"Account created successfully with account number {user_account_number}")
            self.user_data.insert(user_name, user_age, user_address, user_email, user_phone_number, 
                         user_password, user_account_number,user_account_balance)

        except Exception as e:
            print(f"An error occurred: {e}")
