import sqlite3
from datetime import date

from accounts import Accounts

class Transactions:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_table(self) -> None:
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            account_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            debit INTEGER DEFAULT NULL,
            credit INTEGER DEFAULT NULL,
            forfilled INTEGER DEFAULT NULL
        );''')
        self.conn.commit()

    def __debit(self, account: int, amount:int) -> None:
        c = self.conn.cursor()
        today = date.today()
        c.execute('''INSERT INTO transactions (
                date, 
                account_id, 
                debit,
                forfilled
            ) 
            VALUES (?,?,?,?)''', 
            (
                today, 
                account, 
                amount,
                0
            ))
        self.conn.commit()
    
    def __credit(self, account: int, amount:int) -> None:
        c = self.conn.cursor()
        today = date.today()
        c.execute('''INSERT INTO transactions (
                date, 
                account_id, 
                credit,
                forfilled
            ) 
            VALUES (?,?,?,?)''', 
            (
                today, 
                account, 
                amount, 
                0
            ))
        self.conn.commit()


    def send_money(self, 
            from_account: int, 
            to_account: int, 
            amount: int
            ) -> bool:
        """Transfer money from one account to another"""

        try:
            self.__credit(from_account, amount)
            self.__debit(to_account, amount)
            return True
        except Exception as e:
            print(e)
            return False
        
        
