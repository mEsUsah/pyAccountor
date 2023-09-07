import sqlite3

from accounts import Accounts
from transactions import Transactions
import utils
import cli

if __name__ == "__main__":  
    # setup
    cli.splash()
    print("-"*79)
    utils.init_db()
    conn = sqlite3.connect("database.db")
    accounts = Accounts(conn)
    accounts.create_table()
    transactions = Transactions(conn)
    transactions.create_table()
    print("-"*79)
    print()
    
    # menu
    sender, reciver, amount, comment = cli.send_money(accounts.get_all())
    transactions.send_money(sender, reciver, amount, comment)

    conn.close()

