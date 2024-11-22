import os
import json
from datetime import datetime

class TransactionData:

    def __init__(self, file_name):

        """
        Initializes the TransactionData object and loads data from the specified JSON file.
        Parameters:
            file_name (str): The name of the JSON file to load transaction data from.
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

    def save_transaction(self, user_account_number, mode, user_amount_input, updated_amount,
                                                                        bool,account_details):

        try:
            # Create a new dictionary for the account number if it doesn't exist
            if user_account_number not in self.data:
                self.data[user_account_number] = []
            # Get the current date and time as a string
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Create a new transaction record
            if bool:
                transaction_record = {
                    'Mode': mode,
                    'Date_and_time': date_time,
                    'Transaction_amount': user_amount_input,
                    'Updated_amount': updated_amount,
                    'Reciver_Account':account_details
                }
            else:
                  transaction_record = {
                    'Mode': mode,
                    'Date_and_time': date_time,
                    'Transaction_amount': user_amount_input,
                    'Updated_amount': updated_amount,
                    'Sender_Details':account_details
                }

            # Append the new transaction record to the list for the account
            self.data[user_account_number].append(transaction_record)
            # Write the updated data back to the JSON file
            with open(self.json_file, "w") as json_output:
                json.dump(self.data, json_output, indent=4)
        except IOError:
            print(f"Error: Unable to write to the file {self.json_file}.")
        except Exception as e:
            print(f"An unexpected error occurred while inserting data: {e}")
        
    def show_account(self):

        with open(self.json_file,"r") as file:
            data=json.load(file)
        print(data)
