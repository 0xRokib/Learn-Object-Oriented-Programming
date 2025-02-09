# Python Polymorphism

Polymorphism is one of the core concepts of Object-Oriented Programming (OOP) in Python. It allows objects of different classes to be treated as objects of a common superclass. This enables a single interface to be used with different underlying data types.

## Key Features of Polymorphism

- **Method Overriding**: A subclass provides a specific implementation of a method that is already defined in its superclass.
- **Method Overloading (Not Native to Python)**: Python does not support traditional method overloading but can achieve similar behavior using default arguments or variable-length arguments.
- **Operator Overloading**: Python allows operators to have different meanings based on the operands used.

---

## 1. Method Overriding

When a subclass provides a new implementation for a method defined in its parent class.

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"  # Default behavior

class Dog(Animal):
    def make_sound(self):
        return "Bark"  # Overriding method with a specific implementation

class Cat(Animal):
    def make_sound(self):
        return "Meow"  # Overriding method with a specific implementation

# Using polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.make_sound())  # Output: Bark, Meow, Some generic sound
```

---

## 2. Method Overloading (Using Default Arguments)

Python does not support method overloading like Java or C++, but we can achieve similar behavior using default values.

```python
class MathOperations:
    def add(self, a, b, c=0):  # Default argument allows different usage
        return a + b + c

math_op = MathOperations()
print(math_op.add(2, 3))     # Output: 5 (using two arguments)
print(math_op.add(2, 3, 4))  # Output: 9 (using three arguments)
```

---

## 3. Operator Overloading

Python allows overloading of operators using special methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)  # Overloading '+' operator

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Uses __add__ method
print(v3)  # Output: Vector(6, 8)
```

---

## 4. Real-World Example: Payment Processing System

Imagine an e-commerce system where multiple payment methods (CreditCard, PayPal, and Bitcoin) share a common interface.

```python
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")  # Enforces method implementation

# Concrete payment method classes
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        # Simulate validation, authentication, and transaction processing
        return f"Processing credit card payment of ${amount} through Visa/MasterCard."

class PayPalPayment(Payment):
    def process_payment(self, amount):
        # Simulate PayPal API integration
        return f"Processing PayPal payment of ${amount} via secure gateway."

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        # Simulate blockchain transaction confirmation
        return f"Processing Bitcoin payment of ${amount} with blockchain verification."

# Example of a checkout process where payment type is determined at runtime
def checkout(payment_method, amount):
    print(payment_method.process_payment(amount))

# Using polymorphism
payments = [CreditCardPayment(), PayPalPayment(), BitcoinPayment()]
for payment in payments:
    checkout(payment, 100)  # All payment methods use the same interface
```

### Output:

```
Processing credit card payment of $100 through Visa/MasterCard.
Processing PayPal payment of $100 via secure gateway.
Processing Bitcoin payment of $100 with blockchain verification.
```

### Explanation:

- The `Payment` class defines a common interface for all payment methods.
- `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` implement this interface differently.
- The `checkout` function accepts any payment method and processes it without knowing its exact type.
- This allows the system to be easily extended with new payment methods.

This demonstrates polymorphism in a real-world scenario where different payment methods can be used interchangeably with the same interface, making the code more flexible and scalable.

---

## Summary

- **Polymorphism** allows methods in different classes to be called through the same interface.
- **Method overriding** enables subclasses to provide specific implementations.
- **Method overloading** can be mimicked using default parameters.
- **Operator overloading** allows customization of how operators behave with user-defined classes.
- **Real-world applications** include scenarios like payment processing, where multiple implementations of a method exist under a common interface.

Polymorphism increases code reusability and flexibility, making Python more powerful and dynamic!

---
