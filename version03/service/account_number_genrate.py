from constant.constant import ACCOUNT_NUMBER
from model.bank_user_ import UserData

class AccountNumberGenerator:

    def user_account_number_generate(self):

        """
        Generates a new user account number for the banking system.
        This function retrieves existing user data from a JSON file and generates a new 
        account number based on the highest existing account number. If no accounts exist, 
        it uses a predefined constant for the initial account number.
        """
        connection_db=UserData()
        connection_db.display()
        all_data=connection_db.display()
        if len(all_data)==0:
            return ACCOUNT_NUMBER
        else:
            account_number=int(all_data[-1][0])+1
            return str(account_number)
