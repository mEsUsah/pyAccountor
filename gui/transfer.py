import tkinter as tk
import tkinter.ttk as ttk

import utils.db as db


class Tab:
    def __init__(self, tab):
        """This is the transfer tab"""

        transferTab = ttk.Frame(tab)
        transferTab.pack(side="top", expand=False, fill="both")

        self.accounts_list = db.accounts.get_all()
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

        self.from_account_selector = ttk.Combobox(
            from_frame,
            textvariable=self.from_account,
            state='readonly',
            values=self.from_list,
        )
        self.from_account_selector.pack(side="left")
        self.from_account_selector.bind(
            '<<ComboboxSelected>>', 
            self.handle_from_change
        )
        
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
            values=self.to_list,
        )
        self.to_account_selector.pack(side="left")
        self.to_account_selector.bind(
            '<<ComboboxSelected>>', 
            self.handle_to_change
        )


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
        
        
        self.amount_entry = tk.Entry(
            amount_frame,
            width=30,
            validate="all",
            validatecommand=(
                transferTab.register(self.validate_entry_digit), 
                '%P'
            )
        )
        self.amount_entry.pack(side="left")
        self.amount_entry.bind("<KeyPress>", self.handle_amount_change)
        
        # Comment ############################################################
        comment_frame = tk.Frame(transferTab)
        comment_frame.pack(side="top", fill="x")

        comment_label = tk.Label(
            comment_frame,
            text="Comment:",
            width=10,
            anchor="w"
        )
        comment_label.pack(side="left")

        self.comment_entry = tk.Entry(
            comment_frame,
            width=30,
        )
        self.comment_entry.pack(side="left")
        self.comment_entry.bind("<KeyPress>", self.handle_amount_change)

        # Send ###############################################################
        send_frame = tk.Frame(transferTab)
        send_frame.pack(side="top", fill="x")

        self.send_button = tk.Button(
            send_frame,
            text="Transfer money",
            command=self.send_money,
            state="disabled"
        )
        self.send_button.pack(side="left")

    def generate_from_list(self) -> None:
        self.from_list = []
        for account in self.accounts_list:
            self.from_list.append(account['name'])

    def handle_from_change(self, event: tk.Event) -> None:
        self.generate_to_list(event)
        self.check_input_status(event)
    
    def handle_to_change(self, event: tk.Event) -> None:
        self.check_input_status(event)

    def handle_amount_change(self, event: tk.Event) -> None:
        self.check_input_status(event)
    
    def handle_comment_change(self, event: tk.Event) -> None:
        self.check_input_status(event)

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
        self.to_account_selector.bind(
            '<<ComboboxSelected>>', 
            self.handle_to_change
        )

    def validate_entry_digit(self, char):
        return str.isdigit(char) or char == ""
    
    def check_input_status(self, event: tk.Event):
        print("ping")
        if self.from_account.get() != "" \
                and self.to_account.get() != "" \
                and self.amount_entry.get() != "" \
                and self.comment_entry.get() != "":
            self.send_button['state'] = "normal"
        else:
            self.send_button['state'] = "disabled"

    
    def send_money(self) -> None:
        try:
            from_account = db.accounts.get_id(self.from_account.get())
            to_account = db.accounts.get_id(self.to_account.get())
            amount = int(self.amount_entry.get())
            comment = self.comment_entry.get()

            db.transactions.send_money(
                from_account, 
                to_account, 
                amount, 
                comment
            )
        except Exception as e:
            print(e)
