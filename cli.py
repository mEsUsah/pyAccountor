

def list_tables(conn):
    c = conn.cursor()
    for table in c.execute('PRAGMA table_list;'):
        if table[1].startswith("sqlite"):
            continue

        print("-"*10, table[1].center(15), "-"*10, sep="")
        c = conn.cursor()
        for row in c.execute(f"PRAGMA table_info('{table[1]}')"):
            print(row)
        print()

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
        
