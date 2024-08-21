import mysql.connector
from mysql.connector import Error
from config.EnvConfig import EnvConfig

class DbConfig:
    """Class Mysql."""

    def __init__(self):
        self.host = EnvConfig.DB_HOST
        self.username = EnvConfig.DB_USERNAME
        self.password = EnvConfig.DB_PASSWORD
        self.database = EnvConfig.DB_DATABASE
        self.connection = None

    def connect(self):
        """Functcion to Connect DB."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")
        except Error as err:
            print("Error: ", err)

    def disconnect(self):
        """Functcion to Disconnect DB."""
        if self.connection:
            self.connection.close()
            print("Disconnected from MySQL database")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except Error as err:
            print("Error executing query:", err)
            return None
        finally:
            cursor.close()
            self.connection.close()

    def execute_insert(self, query, params):
        self._execute_modify_query(query, params)

    def execute_update(self, query, params):
        self._execute_modify_query(query, params)

    def execute_delete(self, query, params):
        self._execute_modify_query(query, params)

    def _execute_modify_query(self, query, params):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print("Error executing query:", err)
        finally:
            cursor.close()
            self.connection.close()