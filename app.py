import sqlite3

from accounts import Accounts
from transactions import Transactions
import utils
import cli

# Static variables
QUIT = -1
MENU_TRANSFER = 0
MENU_LIST_ACCOUNTS = 1
MENU_SHOW_BALANCE = 2

def handle_menu_selection(selection):
    if selection == MENU_TRANSFER:
        data = cli.send_money(accounts.get_all())
        if data:
            transactions.send_money(*data)
        else:
            return
    elif selection == MENU_LIST_ACCOUNTS:
        accounts.show()
    elif selection == MENU_SHOW_BALANCE:
        account = cli.get_account(accounts.get_all())
        if account == -1:
            return
        else:
            transactions.get_balance(account)


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
        "Show balance",
    )

    while True:
        print("-"*79)
        print("MAIN MENU:")
        main_menu_selected = utils.menu(main_menu_options)
        if main_menu_selected == QUIT:
            break
        
        handle_menu_selection(main_menu_selected)
        
    conn.close()
    exit()
