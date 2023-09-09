import utils


def splash() -> None:
    logo = """
             _____                     _           
     ___ _ _|  _  |___ ___ ___ _ _ ___| |_ ___ ___ 
    | . | | |     |  _|  _| . | | |   |  _| . |  _|
    |  _|_  |__|__|___|___|___|___|_|_|_| |___|_|  
    |_| |___| by Stanley Skarshaug - www.haxor.no
    """
    print(logo)


def send_money(accounts_raw:tuple) -> tuple:
    """Helper menu get needed data to transfer money.

    Returns a tuple with:
    * from_account
    * to_account
    * amount
    * comment
    """

    accounts = {key:value for key, value in accounts_raw }
    print("-"*80)
    
    while True:
        from_account = utils.menu(accounts)
        if from_account == -1:
            return
        else: 
            break
    
    while True:
        to_account = utils.menu(accounts)
        if from_account == -1:
            return
        else: 
            break

    amount = int(input("How much? "))
    comment = input("Comment: ")
    return (from_account, to_account, amount, comment)


def get_account(accounts_raw:tuple) -> int:
    """Helper menu to get account_id
    """
    
    accounts = {key:value for key, value in accounts_raw }
    print("-"*80)
    
    while True:
        account = utils.menu(accounts)
        if account == -1:
            return -1
        else: 
            break
    
    return account
