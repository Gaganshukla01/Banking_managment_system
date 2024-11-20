from model.bank_user_ import UserData
from constant.constant import ACCOUNT_NUMBER

class AccountNumberGenerator:

    user_data = UserData("./model/data.json")

    def __init__(self):
        self.data = self.user_data.display()  
        self.account_number = ACCOUNT_NUMBER  

    def user_account_number_generate(self):
        """
        Generates a new user account number for the banking system.
        This function retrieves existing user data from a JSON file and generates a new 
        account number based on the highest existing account number. If no accounts exist, 
        it uses a predefined constant for the initial account number.
        """
        try:
            if len(self.data) == 0:  # Use self.data to access the instance variable
                account_number = self.account_number
            else:
                last_account_number = list(self.data.keys())[-1]
                account_number = int(last_account_number) + 1  

            return str(account_number)

        except Exception as e:
            print(f"Error: something went wrong {e}")  # Correctly format the error message
