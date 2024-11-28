from constant.constant import ACCOUNT_NUMBER
from model.bank_user_ import UserData

class AccountNumberGenerator:

    def user_account_number_generate(self):

        """
        Generates a new user account number for the banking system.
        This function retrieves existing user data from a JSON file and generates a new 
        account number based on the highest existing account number.
        """

        try:
            connection_db = UserData()
            all_data = connection_db.display()
            if all_data is None:
                print("Error: Unable to retrieve user data.")
                return None
            if len(all_data) == 0:
                return ACCOUNT_NUMBER
            else:
                account_number = int(all_data[-1][0]) + 1
                return str(account_number)

        except ValueError as ve:
            print(f"ValueError: {ve}. Please check the data format.")
            return None
        except TypeError as te:
            print(f"TypeError: {te}. There might be an issue with the data type.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
            