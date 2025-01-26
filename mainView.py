import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, text="Main View", font=("Arial", 18)).pack(pady=20)
        tk.Button(self, 
                  text="Add/Edit Transaction", font=("Arial", 16), 
                  command=lambda: 
                  controller.show_frame("AddEditTransactionView")).pack(pady=10)
        tk.Button(self, 
                  text="View Transactions", 
                  font=("Arial", 16), 
                  command=lambda: 
                  controller.show_frame("ViewTransactionsView")).pack(pady=10)
        tk.Button(self, 
                  text="Generate Reports", 
                  font=("Arial", 16), 
                  command=lambda: 
                  controller.show_frame("GenerateReportsView")).pack(pady=10)
        tk.Button(self, 
                  text="Quit", 
                  font=("Arial", 16), 
                  command=lambda: controller.quit()).pack(pady=20)
    