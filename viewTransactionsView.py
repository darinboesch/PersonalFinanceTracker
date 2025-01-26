import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ViewTransactionsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, 
                 text="View Transactions", 
                 font=("Arial", 18)).pack(pady=20)
        
        cols = ['ID', 'Description', 'Date', 'Amount', 'Category']
        
        self.tree = ttk.Treeview(self, 
                                 columns=cols,
                                 show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in cols:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)

        self.tree.bind("<Double-1>", self.on_double_click)

        tk.Button(self,
                  text="Delete Transaction",
                  font=("Arial", 16),
                  width=20,
                  command=self.delete_selected_transaction).pack(pady=10)
        tk.Button(self, 
                  text="Go Back", 
                  font=("Arial", 16), 
                  width=20,
                  command=lambda: controller.show_frame("MainView")).pack(pady=5)
        
    def refresh(self, transactions):
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for transaction in transactions:
            self.tree.insert('', 
                             tk.END, 
                             values=(transaction.id, 
                                     transaction.description, 
                                     transaction.date, 
                                     transaction.amount, 
                                     transaction.category))
    
    def on_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            selected_values = self.tree.item(selected_item)['values']
            self.controller.edit_transaction(selected_values[0])

    def delete_selected_transaction(self):
        selected_items = self.tree.selection()

        if not selected_items:
            messagebox.showerror("Error", "Please select a transaction to delete")
            return
        
        if not messagebox.askyesno("Delete Transaction", "Are you sure you want to delete the selected transaction?"):
            return
        
        for item in selected_items:
            transaction_id = self.tree.item(item)['values'][0]
            self.controller.delete_transaction(transaction_id)
        