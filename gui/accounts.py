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


        table_headlines = ("ID", "Name")
        table_data = [
            ("1", "test"),
            ("2", "test2"),
        ]
        
        table = ttk.Treeview(
            tab,
            columns=table_headlines,
            show="headings",
            height=7
        )
        for i in range(2):
            table.column(table_headlines[i], anchor="w")
            table.heading(table_headlines[i], text=table_headlines[i],anchor="w")
        table.pack()

        accounts_db = db.accounts
        accounts_list = accounts_db.get_all()
        for row in accounts_list:
            table.insert('','end',values=row)
            

