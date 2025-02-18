class BankAcoount:
    def __init__(self,initial_amount,account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' created.\nBalance = {self.balance:.2f}")
        
    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposite(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.get_balance()