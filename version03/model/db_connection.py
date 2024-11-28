import pymysql

class DatabBaseconnection:

    def connection(self):
        
        try:
            connection_db = pymysql.connect(
                host="localhost",
                user="root",
                password="Password@2024",
                db="banking_system_python"
            )
            cursor = connection_db.cursor()
            return connection_db, cursor

        except pymysql.MySQLError as e:
            print(f"Error connecting to the database: {e}")
            return None, None  

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None, None 
