import tkinter as tk

class GenerateReportsView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")

        tk.Label(self, 
                 text="Generate Reports", 
                 font=("Arial", 18)).pack(pady=20)
        
        self.report_text = tk.Text(self,
                height=15,
                width=50,
                state=tk.DISABLED)
        self.report_text.pack(pady=10)
        
        tk.Button(self, 
                  text="Go Back", 
                  font=("Arial", 16), 
                  command=lambda: controller.show_frame("MainView")).pack(pady=10)
        
    def refresh(self):
        summary = self.controller.get_summary()

        report_lines = [
            f"Total Income: ${summary['income']:.2f}",
            f"Total Expenses: ${summary['expenses']:.2f}",
            f"Net Balance: ${summary['net_balance']:.2f}",
            "Category Summary:"
        ]

        for category, total in summary['category_summary'].items():
            report_lines.append(f"  {category}: ${total:.2f}")

        self.report_text.config(state=tk.NORMAL)
        self.report_text.delete(1.0, tk.END)
        self.report_text.insert(tk.END, "\n".join(report_lines))
        self.report_text.config(state=tk.DISABLED)
        