def splash() -> None:
    logo = """
             _____                     _           
     ___ _ _|  _  |___ ___ ___ _ _ ___| |_ ___ ___ 
    | . | | |     |  _|  _| . | | |   |  _| . |  _|
    |  _|_  |__|__|___|___|___|___|_|_|_| |___|_|  
    |_| |___| by Stanley Skarshaug - www.haxor.no
    """
    print(logo)

def send_money(accounts_raw:tuple) -> None:
    accounts = {key:value for key, value in accounts_raw }
    
    while True:
        for key, value in accounts.items():
            print(key, value, sep=" - ")
        from_account = int(input("Select sender: "))
        if accounts[from_account]:
            print("-"*80)
            break
    
    while True:
        for key, value in accounts.items():
            print(key, value, sep=" - ")
        to_account = int(input("Select receiver: "))
        if accounts[to_account]:
            break

    amount = int(input("How much? "))
    return (from_account, to_account, amount)
        
