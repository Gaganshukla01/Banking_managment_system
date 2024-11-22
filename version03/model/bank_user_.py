import pymysql
from model.db_connection import DatabBaseconnection

class UserData:

    """
    A class to manage user data for a banking system, stored in a MySQL database.
    This class provides methods to insert user data, display existing user data, 
    and update the account balance for a user.
    """

    def __init__(self):

        """
        Initializes the UserData object and sets the cursor for database operations.
        """

        connection_object = DatabBaseconnection()
        self.connection, self.cursor = connection_object.connection()
        self.create_users_table() 

    def create_users_table(self):

        """Create the users table if it does not exist."""

        try:
            sql = """
            CREATE TABLE IF NOT EXISTS users (
                account_number VARCHAR(20) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                address VARCHAR(255),
                phone_number VARCHAR(15),
                password VARCHAR(255) NOT NULL,
                balance INT NOT NULL
            )
            """
            self.cursor.execute(sql)
            self.connection.commit()
        
        except pymysql.MySQLError as e:
            print(f"Error: Unable to create table. {e}")
        except Exception as e:
            print(f"An unexpected error occurred while creating the table: {e}")

    def insert(self, user_name, user_age, user_address, user_email, user_phone_number, 
               user_password, user_account_number, user_account_balance): 
        
        try:
            sql = """
            INSERT INTO users 
            (account_number, name, email, age, address, phone_number, password, balance)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, (user_account_number, user_name, user_email, user_age, 
                        user_address, user_phone_number, user_password, user_account_balance))
            self.connection.commit()  
            print(f"User:{user_name} with account number:{user_account_number} created.")
        
        except pymysql.MySQLError as e:
            print(f"Error: Unable to insert data. {e}")
        except Exception as e:
            print(f"An unexpected error occurred while inserting data: {e}")

    def display(self):

        try:
            sql = "SELECT * FROM users"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results 
        except pymysql.MySQLError as e:
            print(f"Error: Unable to retrieve data. {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while displaying data: {e}")
            return None

    def update_balance(self, user_account_number, new_balance):

        try:
            sql = """
            UPDATE users
            SET balance = %s
            WHERE account_number = %s
            """
            self.cursor.execute(sql, (new_balance, user_account_number))
            self.connection.commit() 
            if self.cursor.rowcount > 0:
                print(f"Balance updated successfully for account number {user_account_number}.")
            else:
                print(f"Account number {user_account_number} does not exist.")
                
        except pymysql.MySQLError as e:
            print(f"Error: Unable to update balance. {e}")
        except Exception as e:
            print(f"An unexpected error occurred while updating balance: {e}")

    def close(self):
        
        """Close the cursor and connection."""
        
        self.cursor.close()
        self.connection.close()
