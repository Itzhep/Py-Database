# PyDB

PyDB is a lightweight and simple disk-based database (DB) for Python. It uses Python's built-in pickle module for serialization and supports both in-memory and file-based databases. PyDB provides a basic set of CRUD (Create, Read, Update, Delete) operations.

## Features

- Easy-to-use interface for managing in-memory or file-based databases
- Thread-safe operations
- Built-in logging
- Support for backups and restores
## online database editor
```bash
http://halekhob.mahanaa.click:8501/
```
## Installation

You can install PyDB using pip:

```bash
pip install pydb
```
## Usage
```bash
from pydb import PyDB

db = PyDB()
```
You can create a new table by calling the create_table method:
```bash
db.create_table('TABELNAME')
```
To insert data into a table, use the insert_data method:
```bash
db.insert_data('users', '1', {'name': 'John Doe', 'email': 'john.doe@example.com'})
```
To retrieve data from a table, use the select_data method:
```bash
data = db.select_data('users', '1')
print(data)  # Output: {'name': 'John Doe', 'email': 'john.doe@example.com'}
```
For backups and restores, use the backup and restore methods, respectively:
```bash
db.backup('backup.pkl')
db.restore('backup.pkl')
```
# PyDB can also be used as a context manager. When used in this way, the database will be automatically saved and closed when the context is exited:
Logging
PyDB automatically logs all database operations to a file named pydb.log. This file is located in the same directory as your Python script.

Contributing
If you would like to contribute to PyDB, please feel free to submit a pull request. Any and all contributions are appreciated.

License
```bash PyDB is licensed under the MIT License. See the LICENSE file for more information. ```

Credits
The pickle module for providing an easy-to-use serialization protocol
The threading module for ensuring thread safety in PyDB operations
The logging module for providing a built-in logging system
The os module for file and directory operations
Feel free to reach out to me at email@example.com if you have any questions or suggestions.

