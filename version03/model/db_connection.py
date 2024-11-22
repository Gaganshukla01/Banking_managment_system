import pymysql

class DatabBaseconnection:

    def connection(self):

        connection_db = pymysql.connect(
            host="localhost",
            user="root",
            password="Password@2024",
            db="banking_system_python"
        )
        cursor = connection_db.cursor()
        
        return connection_db,cursor
       