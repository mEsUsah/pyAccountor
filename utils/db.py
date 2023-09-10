import os

import sqlite3

from models.accounts import Accounts
from models.transactions import Transactions

class Db:
    def __init__(self):
        # setup
        self.init_db()
        self.conn = sqlite3.connect("database.db")
        self.accounts = Accounts(self.conn)
        self.accounts.create_table()
        self.transactions = Transactions(self.conn)
        self.transactions.create_table()
        
    @staticmethod
    def init_db() -> None:
        """create database if not created"""

        DB_FILE = "database.db"

        if not os.path.exists(DB_FILE):
            print("Warning: No DB found... Creating a new one.")
            try:
                file = open(DB_FILE,"w")
                file.close()
                print("Success: Created a new DB")
            except PermissionError:
                print("Error: Did not have permission to crate DB")
                exit()
        else:
            print("Success: Found DB")

db = Db()


