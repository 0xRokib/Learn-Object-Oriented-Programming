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
            
    def transfer_amount(self,amount,account):
        try:
            print("\n********\n\nBeginning Transfer...")
            self.viable_transection(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer Complete! \n\n********")
        except BalanceException as error:
            print(f"Transfer Interrupted: {error}")
            
            
class InterestRewardAccount(BankAcoount):
    def deposite(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite Complete.")
        self.get_balance()
        
class SavingAcount(InterestRewardAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viable_transection(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw Interrupted: {error}")