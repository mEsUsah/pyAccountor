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