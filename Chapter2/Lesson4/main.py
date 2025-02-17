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




# A real-world example of abstraction can be seen in a Payment System:

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