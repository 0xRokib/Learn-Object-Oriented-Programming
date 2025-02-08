# Encapsulation in Python: A Real-World Example

Encapsulation is a fundamental concept in object-oriented programming (OOP) that bundles data (attributes) and methods (functions) into a single unit (class) and restricts direct access to some components. This ensures data integrity, controlled interaction, and modularity.

Let’s start with a **basic example** to understand encapsulation and then refactor it into a more advanced **Bank Account System** example.

---

## Basic Example: A Simple Counter

Let’s create a simple `Counter` class to demonstrate encapsulation.

```python
class Counter:
    def __init__(self):
        self.__count = 0  # Private attribute

    # Public method to increment the counter
    def increment(self):
        self.__count += 1

    # Public method to get the current count
    def get_count(self):
        return self.__count
```

### Explanation:

1. **Private Attribute (`__count`)**:

   - The `__count` attribute is private, meaning it cannot be accessed directly from outside the class.
   - It is prefixed with double underscores (`__`) to enforce name mangling.

2. **Public Methods (`increment` and `get_count`)**:
   - These methods provide controlled access to the private attribute `__count`.
   - `increment` modifies the count, and `get_count` retrieves the current value.

### Example Usage:

```python
counter = Counter()
counter.increment()
counter.increment()
print(counter.get_count())  # Output: 2

# Attempt to access private attribute directly (will raise an error)
# print(counter.__count)  # AttributeError
```

---

## Advanced Example: Bank Account System

Now, let’s refactor the basic example into a more advanced **Bank Account System** to demonstrate encapsulation in a real-world scenario.

---

### Use Case: Bank Account System

In a bank account system:

- The **balance** of an account should not be directly accessible or modifiable by external code.
- Only specific methods like `deposit` and `withdraw` should be allowed to modify the balance.
- The account holder’s **name** can be public, but the **account number** should be protected to prevent accidental changes.
- The **PIN** (used for authentication) should be private and inaccessible from outside the class.

---

### Implementation

```python
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
```

---

### Explanation of the Code

1. **Public Member (`account_holder`)**:

   - The `account_holder` attribute is public, meaning it can be accessed and modified directly from outside the class.
   - Example:
     ```python
     account = BankAccount("John Doe", "123456789", "1234", 1000)
     print(account.account_holder)  # Accessible
     account.account_holder = "Jane Doe"  # Modifiable
     ```

2. **Protected Member (`_account_number`)**:

   - The `_account_number` attribute is marked as protected by prefixing it with a single underscore (`_`).
   - By convention, protected members should only be accessed within the class or its subclasses.
   - Example:
     ```python
     print(account._account_number)  # Accessible but not recommended
     account._account_number = "987654321"  # Modifiable but not recommended
     ```

3. **Private Members (`__pin` and `__balance`)**:

   - The `__pin` and `__balance` attributes are marked as private by prefixing them with double underscores (`__`).
   - Private members cannot be accessed directly from outside the class due to **name mangling**.
   - Example:
     ```python
     # print(account.__pin)  # Raises AttributeError
     # print(account.__balance)  # Raises AttributeError
     ```

4. **Public Methods (`deposit`, `withdraw`, `display_account_info`)**:

   - These methods provide controlled access to the private and protected attributes.
   - For example:
     - `deposit` ensures the amount is valid before updating the balance.
     - `withdraw` validates the PIN and checks if sufficient funds are available before allowing a withdrawal.

5. **Private Method (`__validate_pin`)**:
   - The `__validate_pin` method is private and can only be accessed within the class.
   - It is used internally by the `withdraw` method to validate the user’s PIN.

---

### Example Usage

```python
# Create a bank account
account = BankAccount("John Doe", "123456789", "1234", 1000)

# Display account info
account.display_account_info()
# Output:
# Account Holder: John Doe
# Account Number: 123456789
# Balance: $1000

# Deposit money
account.deposit(500)
# Output: Deposited $500. New balance: $1500

# Withdraw money (valid PIN)
account.withdraw(200, "1234")
# Output: Withdrew $200. New balance: $1300

# Withdraw money (invalid PIN)
account.withdraw(200, "0000")
# Output: Invalid PIN. Withdrawal denied.

# Attempt to access private members directly (will raise an error)
# print(account.__balance)  # AttributeError
# print(account.__pin)  # AttributeError
```

---

### Why This Example Works

1. **Data Protection**:

   - The `__balance` and `__pin` are private, ensuring they cannot be accessed or modified directly.
   - The `_account_number` is protected, discouraging direct access.

2. **Controlled Access**:

   - The `deposit` and `withdraw` methods enforce rules (e.g., validating the PIN and checking the balance) before modifying the account.

3. **Real-World Relevance**:

   - This example mimics a real-world banking system, where sensitive data (like balance and PIN) must be protected, and actions (like deposits and withdrawals) must follow strict rules.

4. **Modularity**:
   - The `BankAccount` class encapsulates all account-related data and methods, making the code modular and reusable.

---

## Key Takeaways

- **Public Members**: Use for attributes and methods that don’t need restrictions (e.g., `account_holder`).
- **Protected Members**: Use for attributes that should only be accessed within the class or its subclasses (e.g., `_account_number`).
- **Private Members**: Use for sensitive data that should not be accessible from outside the class (e.g., `__balance` and `__pin`).
- **Encapsulation**: Ensures data integrity, promotes modularity, and provides controlled access to data.

By applying encapsulation, you can build secure, maintainable, and robust systems, just like a real-world bank account system.
