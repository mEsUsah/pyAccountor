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
        for key, value in accounts.items():
            print(key, value, sep=" - ")
        print("q - Quit / return to menu")
        from_account = input("Select sender: ")
        try:
            if from_account.lower() == "q":
                return
            if accounts[int(from_account)]:
                print("-"*80)
                break
        except ValueError:
            print("Error: You entered an invalid option. Enter a number, or q")
    
    while True:
        for key, value in accounts.items():
            print(key, value, sep=" - ")
        print("q - Quit / return to menu")
        to_account = input("Select receiver: ")
        try:
            if from_account.lower() == "q":
                return
            if accounts[int(to_account)]:
                break
        except ValueError:
            print("Error: You entered an invalid option. Enter a number, or q")

    amount = int(input("How much? "))
    comment = input("Comment: ")
    return (from_account, to_account, amount, comment)
        
