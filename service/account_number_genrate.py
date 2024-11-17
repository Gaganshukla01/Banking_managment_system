from model.bank_user_ import UserData
from constant.constant import ACCOUNT_NUMBER

def user_account_number_genrate():

    """
    Generates a new user account number for the banking system.

    This function retrieves existing user data from a JSON file and generates a new 
    account number based on the highest existing account number. If no accounts exist, 
    it uses a predefined constant for the initial account number.

    The function performs the following steps:
    1. Loads user data from the specified JSON file using the `User Data` class.
    2. Checks if there are existing accounts:
        - If no accounts exist, it uses the constant `ACCOUNT_NUMBER` as the new account number.
        - If accounts exist, it retrieves the last account number, increments it by one, and uses that as the new account number.
    3. Returns the newly generated account number as a string.

    Returns:
        str: The newly generated account number.

    Raises:
        Exception: If an error occurs while loading user data or generating the account number.
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
 