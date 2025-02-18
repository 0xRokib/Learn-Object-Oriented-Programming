from bank_account import *

Rokib = BankAcoount(1000, "Rokib")
# Sara = BankAcoount(2000, "Sara")

# Rokib.get_balance()
# Sara.get_balance()

# Sara.deposite(1000)

# Sara.withdraw(10000)
# Rokib.withdraw(10)

# Rokib.transfer_amount(100, Sara)

Jim = InterestRewardAccount(1000,"Jim")
Jim.get_balance()
Jim.deposite(100)
Jim.transfer_amount(10, Rokib)