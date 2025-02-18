from bank_account import *

Rokib = BankAcoount(1000, "Rokib")
Sara = BankAcoount(2000, "Sara")

Rokib.get_balance()
Sara.get_balance()

Sara.deposite(1000)

Sara.withdraw(10000)
Rokib.withdraw(10)