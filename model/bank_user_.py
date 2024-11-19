import json
import os

class UserData:

    """
    A class to manage user data for a banking system, stored in a JSON file.
    This class provides methods to insert user data, display existing user data, 
    and update the account balance for a user. It handles reading from and writing 
    to a specified JSON file, ensuring that the data is persisted across sessions.
    """

    def __init__(self, file_name):

        """
        Initializes the UserData object and loads data from the specified JSON file.
        """

        self.json_file = file_name
        self.data = {}
        try:
            if os.path.exists(file_name):
                with open(self.json_file, "r") as json_output:
                    self.data = json.load(json_output)
            else:
                self.data = {}

        except FileNotFoundError:
            print(f"Error: The file {file_name} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {file_name} is not a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred while loading the file: {e}")

    def insert(self, user_name, user_age, user_address, user_email, user_phone_number, 
               user_password, user_account_number ,user_account_balance): 
        
        try:
            # Create a new dictionary for the account number if it doesn't exist
            if user_account_number not in self.data:
                self.data[user_account_number] = {}
            self.data[user_account_number]['Name'] = user_name
            self.data[user_account_number]['Email'] = user_email
            self.data[user_account_number]['Age'] = user_age
            self.data[user_account_number]['Address'] = user_address
            self.data[user_account_number]['Phone_Number'] = user_phone_number
            self.data[user_account_number]['Password'] = user_password
            self.data[user_account_number]['Balance'] = user_account_balance 
            with open(self.json_file, "w") as json_output:
                json.dump(self.data, json_output, indent=4)
        
        except IOError:
            print(f"Error: Unable to write to the file {self.json_file}.")
        except Exception as e:
            print(f"An unexpected error occurred while inserting data: {e}")

    def display(self):
        
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, "r") as json_output:
                    data = json.load(json_output)
                    return data  
            else:
                print(f"{self.json_file} is not created yet")
                return None

        except FileNotFoundError:
            print(f"Error: The file {self.json_file} was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file {self.json_file} is not a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred while displaying data: {e}")
            return None

    def update_balance(self, user_account_number, new_balance):
        
        try:
            if user_account_number in self.data:
                self.data[user_account_number]['Balance'] = new_balance
                with open(self.json_file, "w") as json_output:
                    json.dump(self.data, json_output, indent=4)
                print(f"Balance updated successfully for account number {user_account_number}.")
            else:
                print(f"Account number {user_account_number} does not exist.")
                
        except IOError:
            print(f"Error: Unable to write to the file {self.json_file}.")
        except Exception as e:
            print(f"An unexpected error occurred while updating balance: {e}")
