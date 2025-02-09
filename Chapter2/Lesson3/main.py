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
    checkout(payment, 100)