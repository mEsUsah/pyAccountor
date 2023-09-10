import tkinter as tk
import tkinter.ttk as ttk

import utils.db as db


class Tab:
    def __init__(self, tab):
        """This is the accounts tab"""

        accountsTab = ttk.Frame(tab)
        accountsTab.pack(side="top", expand=1, fill="both")

        tab_label = ttk.Label(
            accountsTab,
            text="All accounts"
        )
        tab_label.pack(side="top", fill="x", padx=10, pady=6)

        table_headlines = ("ID", "Name", "Balance")
        table = ttk.Treeview(
            tab,
            columns=table_headlines,
            show="headings",
            height=7
        )
        for i in range(len(table_headlines)):
            table.column(table_headlines[i], anchor="w")
            table.heading(table_headlines[i], text=table_headlines[i],anchor="w")
        table.pack()

        accounts_db = db.accounts
        accounts_list = accounts_db.get_all()
        for row in accounts_list:
            row['balance'] = db.transactions.get_balance(int(row['id']))
            print(row)
            table.insert(
                '',
                'end',
                values=(row['id'], row['name'], row['balance'])
            )
            

