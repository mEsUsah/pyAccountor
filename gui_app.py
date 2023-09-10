import tkinter as tk
from tkinter import ttk

import gui

window = tk.Tk()
window.title("pyAccountor")
window.geometry("-100+100")
# window.resizable(False,False)

mainTabControl = ttk.Notebook(window)

accountsTab =  ttk.Frame(mainTabControl)
transferTab =  ttk.Frame(mainTabControl)
mainTabControl.add(accountsTab, text="Accounts")
mainTabControl.add(transferTab, text="Transfer")

mainTabControl.pack(expand=1, fill="both")

accounts = gui.accounts.Tab(accountsTab)
transfer = gui.transfer.Tab(transferTab)


# Credits
bottomFrame = ttk.Frame(window)
bottomFrame.pack(side="bottom", fill="x")
versionLabel = ttk.Label(bottomFrame, text="v1.0.0")
versionLabel.pack(side="right", fill="x", padx=10, pady=10)

creditsLabel = ttk.Label(
    bottomFrame, 
    text="Created by Stanley Skarshaug - www.haxor.no"
)
creditsLabel.pack(side="left", fill="x", padx=10, pady=10)

window.mainloop()