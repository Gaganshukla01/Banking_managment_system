from datetime import datetime
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

    def show_account(self):
        pass
    