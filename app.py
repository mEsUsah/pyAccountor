import sqlite3

from accounts import Accounts
from transactions import Transactions
import utils
import cli

# Static variables
TRANSFER = 0
LIST_ACCOUNTS = 1

def handle_menu_selection(selection):
    if selection == TRANSFER:
        data = cli.send_money(accounts.get_all())
        if data:
            transactions.send_money(*data)
        else:
            return
    elif selection == LIST_ACCOUNTS:
        accounts.show()


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
    
    # menu
    main_menu_options = (
        "Transfer money",
        "List accounts",
        "Exit program",
    )

    while True:
        print("-"*79)
        print("MAIN MENU:")
        main_menu_selected = utils.menu(main_menu_options)
        if main_menu_selected == len(main_menu_options) - 1:
            break
        
        handle_menu_selection(main_menu_selected)
        
    conn.close()
    exit()
