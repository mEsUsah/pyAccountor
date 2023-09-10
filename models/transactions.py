import sqlite3
from datetime import date

from models.accounts import Accounts

class Transactions:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def create_table(self) -> None:
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            account_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            comment TEXT,
            debit INTEGER DEFAULT NULL,
            credit INTEGER DEFAULT NULL,
            fulfilled INTEGER DEFAULT NULL
        );''')
        self.conn.commit()

    def __debit(self, account: int, amount:int, comment:str) -> None:
        c = self.conn.cursor()
        today = date.today()
        c.execute('''INSERT INTO transactions (
                date, 
                account_id, 
                debit,
                comment,
                fulfilled
            ) 
            VALUES (?,?,?,?,?)''', 
            (
                today, 
                account, 
                amount,
                comment,
                False
            ))
        self.conn.commit()
    
    def __credit(self, account: int, amount:int, comment:str) -> None:
        c = self.conn.cursor()
        today = date.today()
        c.execute('''INSERT INTO transactions (
                date, 
                account_id, 
                credit,
                comment,
                fulfilled
            ) 
            VALUES (?,?,?,?,?)''', 
            (
                today, 
                account, 
                amount,
                comment,
                False
            ))
        self.conn.commit()

    def get_balance(self, account: int) -> None:
        c = self.conn.cursor()
        query = f'''SELECT sum(debit), sum(credit) FROM transactions
            WHERE account_id = {account};'''

        c.execute(query)
        debit, credit = c.fetchone()
        if debit is None:
            debit = 0
        if credit is None:
            credit = 0

        balance = debit - credit
        
        print(f"The current balance is: {balance}")


    def get_transactions(self, account: int) -> None:
        print("+" + "-"*13 + "+" + "-"*51 + "+" + "-"*10 + "+")
        print("| Date".ljust(14) + "| Comment".ljust(52) + "|" + "Amount ".rjust(10) + "|")
        print("+" + "-"*13 + "+" + "-"*51 + "+" + "-"*10 + "+")
        c = self.conn.cursor()
        query = f'''SELECT date, comment, debit, credit FROM transactions
            WHERE account_id = {account};'''
        
        for row in c.execute(query):
            if row[1] is None:
                comment = ""
            else:
                comment = row[1]
            
            if row[2] is not None:
                amount = str(row[2])
            else:
                amount = "-" + str(row[3]) # credit
            
            print("| " + row[0].ljust(12) + "| " + comment.ljust(50) + "| " + amount.rjust(8) + " |")
        
        print("+" + "-"*13 + "+" + "-"*51 + "+" + "-"*10 + "+")

    def send_money(self, 
            from_account: int, 
            to_account: int, 
            amount: int,
            comment: str,
            ) -> bool:
        """Transfer money from one account to another"""

        try:
            self.__credit(from_account, amount, comment)
            self.__debit(to_account, amount, comment)
            return True
        except Exception as e:
            print(e)
            return False
        
        
