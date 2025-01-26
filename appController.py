import tkinter as tk

from appModel import AppModel
from transactionModel import TransactionModel

from mainView import MainView
from addEditTransactionView import AddEditTransactionView
from viewTransactionsView import ViewTransactionsView
from generateReportsView import GenerateReportsView

class AppController:
    def __init__(self):
        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")

        #Create the models
        self.model = AppModel()
        self.transaction_model = TransactionModel()

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        
        # Populate the frames dictionary with the views
        for view_name in [ MainView, 
                          AddEditTransactionView, 
                          ViewTransactionsView, 
                          GenerateReportsView ]:
            frame = view_name(self.container, self)
            self.frames[view_name.__name__] = frame

        # Show the main view
        self.show_frame("MainView")

    def show_frame(self, view_name, transaction=None):
        if view_name == "AddEditTransactionView":
            self.frames[view_name].set_transaction(transaction)
        if view_name == "ViewTransactionsView":
            self.frames[view_name].refresh(self.transaction_model.transactions)
        if view_name == "GenerateReportsView":
            self.frames[view_name].refresh()        

        frame = self.frames[view_name]
        frame.tkraise()

    def save_transaction(self, transaction):
        if any(tx.id == transaction.id for tx in self.transaction_model.transactions):
            self.transaction_model.update_transaction(transaction)
        else:
            self.transaction_model.add_transaction(transaction)
        
        self.show_frame("MainView")

    def edit_transaction(self, transaction_id):
        transaction = next((tx for tx in self.transaction_model.transactions if tx.id == transaction_id), None)
        self.show_frame("AddEditTransactionView", transaction)

    def delete_transaction(self, transaction_id):
        self.transaction_model.delete_transaction(transaction_id)
        self.show_frame("ViewTransactionsView")

    def get_summary(self):
        return self.transaction_model.get_summary()

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.quit()