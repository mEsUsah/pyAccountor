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
        self.from_list = []
        self.to_list = []
        self.generate_from_list()

        self.from_account = tk.StringVar()
        self.to_account = tk.StringVar()

        # From ###############################################################
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
            state='readonly',
            values=self.from_list,
        )
        from_account_selector.pack(side="left")
        from_account_selector.bind('<<ComboboxSelected>>',self.generate_to_list)
        
        # To #################################################################
        self.to_frame = tk.Frame(transferTab)
        self.to_frame.pack(side="top", fill="x", expand=True)

        to_label = tk.Label(
            self.to_frame,
            text="To:",
            width=10,
            anchor="w"
        )
        to_label.pack(side="left")

        self.to_account_selector = ttk.Combobox(
            self.to_frame,
            textvariable=self.to_account,
            state='readonly',
            values=self.to_list
        )
        self.to_account_selector.pack(side="left")

        # Amount #############################################################
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
            validate="all",
            validatecommand=(
                transferTab.register(self.validate_entry_digit), 
                '%P'
            )
        )
        amount_entry.pack(side="left")
        
        # Comment #############################################################
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

    def generate_from_list(self) -> None:
        self.from_list = []
        for account in self.accounts_list:
            self.from_list.append(account['name'])

    def generate_to_list(self, event: tk.Event) -> None:
        self.to_list = []
        self.to_account.set("")
        selected_to = event.widget.get()
        for account in self.accounts_list:
            if account['name'] != selected_to:
                self.to_list.append(account['name'])

        self.to_account_selector.destroy()
        
        self.to_account_selector = ttk.Combobox(
            self.to_frame,
            textvariable=self.to_account,
            state='readonly',
            values=self.to_list
        )
        self.to_account_selector.pack(side="left")

    def validate_entry_digit(self, char):
        return str.isdigit(char) or char == ""