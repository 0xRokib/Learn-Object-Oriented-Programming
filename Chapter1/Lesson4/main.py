class BankAccount:
    def __init__(self, account_holder, account_number, pin, initial_balance=0):
        self.account_holder = account_holder  # Public attribute
        self._account_number = account_number  # Protected attribute
        self.__pin = pin  # Private attribute
        self.__balance = initial_balance  # Private attribute

    # Public method to display account details
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: ${self.__balance}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):  # Validate PIN before allowing withdrawal
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds or invalid amount.")
        else:
            print("Invalid PIN. Withdrawal denied.")

    # Private method to validate PIN
    def __validate_pin(self, pin):
        return self.__pin == pin
    
    
# Create a bank account for John Doe
account = BankAccount("John Doe", "123456789", "1234", 1000)

# Display account information
account.display_account_info()
# Output:
# Account Holder: John Doe
# Account Number: 123456789
# Balance: $1000



# Deposit $500 into the account
account.deposit(500)
# Output: Deposited $500. New balance: $1500
# Attempt to deposit an invalid amount (e.g., -$100)
account.deposit(-100)
# Output: Invalid deposit amount.



# Withdraw $200 (valid PIN)
account.withdraw(200, "1234")
# Output: Withdrew $200. New balance: $1300
# Attempt to withdraw with an invalid PIN
account.withdraw(200, "0000")
# Output: Invalid PIN. Withdrawal denied.
# Attempt to withdraw more than the available balance
account.withdraw(2000, "1234")
# Output: Insufficient funds or invalid amount.




# Accessing public member (account_holder)
print(account.account_holder)  # Output: John Doe
# Modifying public member (account_holder)
account.account_holder = "Jane Doe"
print(account.account_holder)  # Output: Jane Doe
# Accessing protected member (_account_number)
print(account._account_number)  # Output: 123456789
# Attempting to access private members (__balance and __pin)
# This will raise an AttributeError
try:
    print(account.__balance)
except AttributeError as e:
    print(e)  # Output: 'BankAccount' object has no attribute '__balance'
try:
    print(account.__pin)
except AttributeError as e:
    print(e)  # Output: 'BankAccount' object has no attribute '__pin'
    
    
# Display updated account information
account.display_account_info()
# Output:
# Account Holder: Jane Doe
# Account Number: 123456789
# Balance: $1300