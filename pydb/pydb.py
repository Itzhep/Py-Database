import pickle
import os
import threading
import logging
from io import BytesIO
import re
class PyDB:
    def __init__(self, db_file=None):
        self.db_file = db_file
        self.data = self.load_data()
        self.lock = threading.Lock()
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='pydb.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def log_query(self, query):
        logging.info(f"Query: {query}")

    def load_data(self):
        if self.db_file is not None:
            if hasattr(self.db_file, 'read'):
                self.db_file.seek(0)
                try:
                    return pickle.load(self.db_file)
                except (EOFError, pickle.UnpicklingError):
                    return {}
            elif os.path.exists(self.db_file):
                with open(self.db_file, 'rb') as file:
                    return pickle.load(file)
        return {}

    def save_data(self):
        with self.lock:
            if self.db_file is not None:
                if hasattr(self.db_file, 'write'):
                    self.db_file.seek(0)
                    self.db_file.truncate()
                    self.db_file.write(pickle.dumps(self.data))
                else:
                    with open(self.db_file, 'wb') as file:
                        pickle.dump(self.data, file)

    def create_table(self, table_name):
        with self.lock:
            if table_name not in self.data:
                self.data[table_name] = {}
                self.save_data()
                self.log_query(f"CREATE TABLE {table_name}")

    def insert_data(self, table_name, key, value):
        with self.lock:
            if table_name not in self.data:
                raise ValueError(f"Table '{table_name}' does not exist.")

            self.data[table_name][key] = value
            self.save_data()
            self.log_query(f"INSERT INTO {table_name} ({key}, {value})")

    def select_data(self, table_name, key):
        with self.lock:
            if table_name not in self.data or key not in self.data[table_name]:
                return None

            return self.data[table_name][key]

    def backup(self, backup_file):
        with self.lock:
            try:
                with open(backup_file, 'wb') as file:
                    pickle.dump(self.data, file)
                print("Backup created successfully.")
            except Exception as e:
                print(f"Backup failed: {str(e)}")

    def restore(self, backup_file):
        with self.lock:
            try:
                with open(backup_file, 'rb') as file:
                    self.data = pickle.load(file)
                self.save_data()
                print("Restore completed successfully.")
            except Exception as e:
                print(f"Restore failed: {str(e)}")
    def execute(self, query):
        with self.lock:
            # You can add more query types as needed
            if query.startswith("CREATE TABLE"):
                self.create_table(query)
            elif query.startswith("INSERT INTO"):
                self.execute_insert(query)
            # Add more query types as needed

    def execute_insert(self, query):
        # Extract table name, key, and value from the INSERT query
        match = re.match(r"INSERT INTO (\w+) \((\w+), (.+)\)", query)
        if match:
            table_name = match.group(1)
            key = match.group(2)
            value = eval(match.group(3))  # Use eval to convert the string to a Python object
        else:
            raise ValueError("Invalid INSERT INTO query")

        if table_name not in self.data:
            raise ValueError(f"Table '{table_name}' does not exist.")

        self.data[table_name][key] = value
        self.save_data()
        self.log_query(query)
    def close(self):
        self.save_data()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

