import tkinter as tk
from datetime import datetime 
from transaction import Transaction

class AddEditTransactionView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller        

        self.transaction = None
        self.id = tk.IntVar()
        self.description = tk.StringVar()
        self.date = tk.StringVar(value=datetime.now().strftime('%m/%d/%Y'))
        self.amount = tk.DoubleVar()
        self.category = tk.StringVar()

        self.init_ui()

    def init_ui(self):
        self.grid(row=0, column=0, sticky="nsew")
        tk.Label(self, 
                 text="Add/Edit Transaction", 
                 font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)        
        labels = ['ID', 'Description', 'Date', 'Amount', 'Category']
        variables = [self.id, self.description, self.date, self.amount, self.category]

        for index, (label, variable) in enumerate(zip(labels, variables)):
            tk.Label(self, 
                     text=label,
                     font=("Arial", 16 )).grid(row=index+1, 
                                               column=0, 
                                               sticky='e', 
                                               padx=10,
                                               pady=5)
            entry = tk.Entry(self, textvariable=variable)
            entry.grid(row=index + 1, 
                       column=1, 
                       sticky='w', 
                       padx=10, 
                       pady=5)
            
            if label == 'ID':
                entry.config(state='readonly')

        tk.Button(self, 
                  text="Save", 
                  font=("Arial", 16), 
                  command=self.save_transaction).grid(row=6, column=1, columnspan=2, pady=10, sticky='w')
        tk.Button(self, 
                  text="Go Back", 
                  font=("Arial", 16), 
                  command=lambda: self.controller.show_frame("MainView")).grid(row=6, column=0, columnspan=2, pady=10, sticky='e')
    
    def set_transaction(self, transaction):
        if transaction:
            self.transaction = transaction
            self.id.set(transaction.id)
            self.description.set(transaction.description)
            self.date.set(transaction.date)
            self.amount.set(transaction.amount)
            self.category.set(transaction.category)
        else:
            self.transaction = None
            self.id.set(0)
            self.description.set('')
            self.date.set(datetime.now().strftime('%m/%d/%Y'))
            self.amount.set(0)
            self.category.set('')
    
    def save_transaction(self):
        transaction = Transaction(self.id.get(), 
                                  self.description.get(), 
                                  self.date.get(), 
                                  self.amount.get(), 
                                  self.category.get())
        self.controller.save_transaction(transaction)
