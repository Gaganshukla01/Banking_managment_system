from model.bank_user_ import UserData
from constant.constant import ACCOUNT_NUMBER

def user_account_number_genrate():

    """
    Generates a new user account number for the banking system.
    This function retrieves existing user data from a JSON file and generates a new 
    account number based on the highest existing account number. If no accounts exist, 
    it uses a predefined constant for the initial account number.
    """

    try:
        user_data = UserData("./model/data.json")
        data = user_data.display()
        account_number=ACCOUNT_NUMBER
        if len(data) == 0:  
            account_number=ACCOUNT_NUMBER
        else:
            last_account_number = list(data.keys())[-1]
            account_number = int(last_account_number) + 1  

        return str(account_number)

    except Exception as e:
        print("Error:something went wrong {e}")
 