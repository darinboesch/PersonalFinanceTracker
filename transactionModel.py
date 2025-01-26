import json

from transaction import Transaction

class TransactionModel:
    FILE_NAME = 'transactions.json'

    def __init__(self):
        self.transactions = self._load_transactions()

    def _load_transactions(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                return [Transaction.from_dict(transaction) for transaction in json.load(file)]
        except FileNotFoundError:
            return []
        
    def _save_transactions(self):
        with open(self.FILE_NAME, 'w') as file:
            json.dump([transaction.to_dict() for transaction in self.transactions], file)

    def add_transaction(self, transaction):
        transaction.id = self.get_unique_id()
        self.transactions.append(transaction)
        self._save_transactions()

    def get_unique_id(self):
        return max([transaction.id for transaction in self.transactions] + [0]) + 1
    
    def update_transaction(self, updated_transaction):
        for index, transaction in enumerate(self.transactions):
            if transaction.id == updated_transaction.id:
                self.transactions[index] = updated_transaction
                self._save_transactions()
                return
            
    def delete_transaction(self, transaction_id):
        self.transactions = [transaction for transaction in self.transactions if transaction.id != transaction_id]
        self._save_transactions()

    def get_summary(self):
        income = sum([transaction.amount for transaction in self.transactions if transaction.amount > 0])
        expenses = sum([transaction.amount for transaction in self.transactions if transaction.amount < 0])
        net_balance = income + expenses

        category_summary = {}
        for transaction in self.transactions:
            if transaction.category not in category_summary:
                category_summary[transaction.category] = 0
            
            category_summary[transaction.category] += transaction.amount

        return {
            "income": income,
            "expenses": expenses,
            "net_balance": net_balance,
            "category_summary": category_summary
        }
            
if __name__ == "__main__":
    transaction_model = TransactionModel()
    print(transaction_model.transactions)
    
    transaction = Transaction(None, 'Test', '2021-01-01', 100, 'Test')
    transaction_model.add_transaction(transaction)

    print(transaction_model.transactions)

    transaction.description = 'Updated'
    transaction_model.update_transaction(transaction)

    print(transaction_model.transactions)
