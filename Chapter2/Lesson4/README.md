# Python OOP: Abstraction

## Introduction

Abstraction is one of the fundamental principles of Object-Oriented Programming (OOP). It is used to hide the implementation details of a class and only show the essential features. In Python, abstraction is implemented using abstract classes and abstract methods.

The `abc` module (Abstract Base Class) provides the functionality to create abstract classes in Python. An abstract class cannot be instantiated and serves as a blueprint for other classes.

## Example Code

The following example demonstrates the concept of abstraction in Python:

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

# vehicle = Vehicle()  # This will raise an error since Vehicle is an abstract class
car = Car()
motorcycle = Motorcycle()

# Calling methods
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
```

## Explanation

1. **Abstract Class (`Vehicle`)**:

   - It is defined using the `ABC` class from the `abc` module.
   - It contains two abstract methods: `go()` and `stop()`, which do not have implementations.
   - This class cannot be instantiated.

2. **Concrete Classes (`Car` and `Motorcycle`)**:

   - These classes inherit from `Vehicle`.
   - They provide implementations for the `go()` and `stop()` methods.

3. **Usage**:
   - If we try to instantiate `Vehicle`, it will raise a `TypeError` since it has abstract methods.
   - `Car` and `Motorcycle` implement all the abstract methods, so they can be instantiated and used.

## Output

When the above script is executed, the following output is produced:

```
You drive the car
You ride the motorcycle
This car is stopped
This motorcycle is stopped
```

## Real-World Example

A real-world example of abstraction can be seen in a **Payment System**:

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):

    def make_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):

    def make_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# payment = Payment()  # This will raise an error since Payment is an abstract class
credit_card = CreditCardPayment()
paypal = PayPalPayment()

# Calling methods
credit_card.make_payment(100)
paypal.make_payment(200)
```

### Explanation:

- The `Payment` class is an abstract class with an abstract method `make_payment()`.
- `CreditCardPayment` and `PayPalPayment` are concrete classes that implement the `make_payment()` method.
- This ensures that all payment methods follow a standard structure while allowing different implementations.

## Why Use Abstraction?

- Ensures that subclasses provide specific implementations for the abstract methods.
- Provides a blueprint for related classes.
- Improves code reusability and maintainability.

## Conclusion

Abstraction in Python allows developers to define a standard interface for a group of related classes. This ensures that all derived classes implement the required methods, making the code more structured and scalable.
