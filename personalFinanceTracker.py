from appController import AppController

class PersonalFinanceTracker:
    def __init__(self):
        self.appController = AppController()

    def run(self):
        self.appController.run()

if __name__ == "__main__":
    app = PersonalFinanceTracker()
    app.run()        