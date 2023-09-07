import sqlite3

class Accounts:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_table(self) -> None:
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );''')
        self.conn.commit()

    def add(self, name: str) -> bool:
        c = self.conn.cursor()
        try:
            c.execute('INSERT INTO accounts (name) VALUES (?)', (name,))
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def show(self) -> None:
        c = self.conn.cursor()
        for row in c.execute('SELECT * FROM accounts'):
            print(row)

    def get_all(self):
        c = self.conn.cursor()
        return c.execute('SELECT * FROM accounts')

    def get(self, id) -> tuple:
        c = self.conn.cursor()
        c.execute(f'''SELECT * FROM accounts WHERE id = {id};''')
        return c.fetchone()
        