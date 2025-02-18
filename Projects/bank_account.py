class BalanceException(Exception):
    pass

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
        
    def viable_transection(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try:
            self.viable_transection(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw Interrupted: {error}")
            