class Transaction:
    def __init__(self, id, description, date, amount, category):
        self.id = id
        self.description = description
        self.date = date
        self.amount = amount
        self.category = category

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'date': self.date,
            'amount': self.amount,
            'category': self.category
        }
    
    @staticmethod
    def from_dict(data):
        return Transaction(
            data['id'], 
            data['description'], 
            data['date'], 
            data['amount'], 
            data['category'])