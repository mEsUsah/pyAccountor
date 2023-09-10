import tkinter as tk
import tkinter.ttk as ttk

import utils.db as db


class Tab:
    def __init__(self, tab):
        """This is the transfer tab"""

        transferTab = ttk.Frame(tab)
        transferTab.pack(side="top", expand=False, fill="both")

        accounts_db = db.accounts
        self.accounts_list = accounts_db.get_all()
        self.from_account = tk.StringVar()
        self.to_account = tk.StringVar()
        print(self.accounts_list)

        # From
        from_frame = tk.Frame(transferTab)
        from_frame.pack(side="top", fill="x", expand=True)

        from_label = tk.Label(
            from_frame,
            text="From:",
            width=10,
            anchor="w"
        )
        from_label.pack(side="left")

        from_account_selector = ttk.Combobox(
            from_frame,
            textvariable=self.from_account,
            state='readonly'
        )
        from_account_selector.pack(side="left")
        
        # To
        to_frame = tk.Frame(transferTab)
        to_frame.pack(side="top", fill="x", expand=True)

        to_label = tk.Label(
            to_frame,
            text="To:",
            width=10,
            anchor="w"
        )
        to_label.pack(side="left")

        to_account_selector = ttk.Combobox(
            to_frame,
            textvariable=self.to_account,
            state='readonly',
        )
        to_account_selector.pack(side="left")

        # Amount
        amount_frame = tk.Frame(transferTab)
        amount_frame.pack(side="top", fill="x")

        amount_label = tk.Label(
            amount_frame,
            text="Amount:",
            width=10,
            anchor="w"
        )
        amount_label.pack(side="left")

        amount_entry = tk.Entry(
            amount_frame,
            width=30,
        )
        amount_entry.pack(side="left")
        
        # Amount
        comment_frame = tk.Frame(transferTab)
        comment_frame.pack(side="top", fill="x")

        comment_label = tk.Label(
            comment_frame,
            text="Comment:",
            width=10,
            anchor="w"
        )
        comment_label.pack(side="left")

        comment_entry = tk.Entry(
            comment_frame,
            width=30,
        )
        comment_entry.pack(side="left")



