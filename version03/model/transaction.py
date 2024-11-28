from datetime import datetime
from tabulate import tabulate
from model.db_connection import DatabBaseconnection

class TransactionData:

    def __init__(self):

        self.db_connection = DatabBaseconnection()
        self.connection, self.cursor = self.db_connection.connection()
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.create_table()

    def create_table(self):

        sql = """
            CREATE TABLE IF NOT EXISTS transaction (
                txn_id INT AUTO_INCREMENT PRIMARY KEY,
                date_time VARCHAR(45),
                account_number INT,
                mode VARCHAR(30),
                transaction_amount INT,
                updated_amount INT,
                receiver_account VARCHAR(45),
                sender_account VARCHAR(45)
            )
        """
        self.cursor.execute(sql)
        self.connection.commit()

    def save_transaction(self, user_account_number, mode, user_amount_input, 
                        updated_amount, is_successful, account_details):

        query = """
            INSERT INTO transaction (date_time, account_number, mode, transaction_amount, updated_amount, receiver_account, sender_account)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            if mode=="Transfer":
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, account_details, "NA"))
                self.connection.commit()
                print("Sender account updated")
            elif mode=="Received":
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, "NA", account_details))
                self.connection.commit()
                print("Reciver account updated")
            else:
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, "NA", "NA"))
                self.connection.commit()
                print("Transaction saved successfully")    
        except Exception as e:
            print(f"Error saving transaction: {e}")
            self.connection.rollback()

    def save_transaction(self, user_account_number, mode, user_amount_input, 
                        updated_amount, is_successful, account_details):
        query = """
            INSERT INTO transaction (date_time, account_number, mode, transaction_amount, updated_amount, receiver_account, sender_account)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            if mode == "Transfer":
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, account_details, "NA"))
                self.connection.commit()
                print("Sender account updated")
            elif mode == "Received":
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, "NA", account_details))
                self.connection.commit()
                print("Receiver account updated")
            else:
                self.cursor.execute(query, (self.date_time, user_account_number, mode, user_amount_input, updated_amount, "NA", "NA"))
                self.connection.commit()
                print("Transaction saved successfully")    
        except Exception as e:
            print(f"Error saving transaction: {e}")
            self.connection.rollback()

    def show_transaction_history(self, account_number):
        """
        Fetches and displays the transaction history for a given account number in a table format.
        """
        query = "SELECT * FROM transaction WHERE account_number = %s"
        try:
            self.cursor.execute(query, (account_number,))
            transactions = self.cursor.fetchall()

            if transactions:
                # Prepare the table headers and rows
                headers = ["Transaction ID", "Date/Time", "Account Number", "Mode", "Transaction Amount", "Updated Amount", "Receiver Account", "Sender Account"]
                table = []

                for txn in transactions:
                    table.append([txn[0], txn[1], txn[2], txn[3], txn[4], txn[5], txn[6], txn[7]])

                # Print the table using tabulate
                print(f"Transaction history for account number {account_number}:")
                print(tabulate(table, headers=headers, tablefmt="grid"))
            else:
                print(f"No transactions found for account number {account_number}.")
        except Exception as e:
            print(f"Error fetching transaction history: {e}")

    def show_account_details(self, account_number):
     
        query = "SELECT * FROM users WHERE account_number = %s"  
        try:
            self.cursor.execute(query, (account_number,))
            account_details = self.cursor.fetchone()

            if account_details:
                print(f"Account holder name: {account_details[1]}\nAccount Number: {account_details[0]}\nBalance: {account_details[7]}")  
            else:
                print(f"No account found with account number {account_number}.")
        except Exception as e:
            print(f"Error fetching account details: {e}")
   