import sqlite3

from accounts import Accounts
from transactions import Transactions
import cli

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    accounts = Accounts(conn)
    accounts.create_table()
    transactions = Transactions(conn)
    transactions.create_table()
    
    # create_tables()
    # list_tables()


    sender, reciver, amount = cli.send_money(accounts.get_all())
    transactions.send_money(sender, reciver, amount)

    conn.close()

