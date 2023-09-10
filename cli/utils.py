import os

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



def list_tables(conn) -> None:
    """list all project tables in database"""

    c = conn.cursor()
    for table in c.execute('PRAGMA table_list;'):
        if table[1].startswith("sqlite"):
            continue

        print("-"*10, table[1].center(15), "-"*10, sep="")
        c = conn.cursor()
        for row in c.execute(f"PRAGMA table_info('{table[1]}')"):
            print(row)
        print()

def menu(options) -> int:  
    """ Simple CLI menu system:

    * Options must of type list, tuple or dictionary
    * Dictionary must use numeric keys

    Returns the list or tuple index selected, or dictionary key.
    NOTE: If quit is selected it will return -1.
    """

    if isinstance(options, list) or isinstance(options, tuple):
        options_type = "simple"
    elif isinstance(options, dict):
        options_type = "dict"

    if options_type == "simple":
        for i, option in enumerate(options):
            print(f'{i + 1}: {option}')
    elif options_type == "dict":
        for key, value in options.items():
            print(f'{key}: {value}')

    print("Q: quit")

    while True:
        try:
            selected = input('Select: ')
            if selected.lower() == "q":
                return -1
            selected = int(selected)
        except ValueError:
            print('Error, invalid selection. ', end="")
            continue
        
        if options_type == "simple":
            if selected > 0 and selected <= len(options):
                selected -= 1
                break

        elif options_type == "dict":
            if selected in options:
                break

    return selected