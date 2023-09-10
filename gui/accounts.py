import tkinter as tk
import tkinter.ttk as ttk

import utils.db as db


class Tab:
    def __init__(self, tab):
        """This is the accounts tab"""

        accountsTab = ttk.Frame(tab)
        accountsTab.pack(side="top", expand=1, fill="both")

        accounts_db = db.accounts
        accounts_list = accounts_db.get_all()

        table_headlines = ("ID", "Name", "Balance")
        table = ttk.Treeview(
            tab,
            columns=table_headlines,
            show="headings",
            height=len(accounts_list),
        )
        for i in range(len(table_headlines)):
            if i == 2:
                anchor = "e"
            else:
                anchor = "w"
            
            table.column(table_headlines[i], anchor=anchor)
            table.heading(
                table_headlines[i], 
                text=table_headlines[i],
                anchor=anchor,
            )
        table.pack()

        for row in accounts_list:
            row['balance'] = db.transactions.get_balance(int(row['id']))
            print(row)
            table.insert(
                '',
                'end',
                values=(row['id'], row['name'], row['balance'])
            )
            

