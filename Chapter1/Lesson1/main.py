# main.py
# A simple example of Object-Oriented Programming (OOP) in Python

# Define a class
class Dog:
    # Constructor (initializes attributes)
    def __init__(self, name, age):
        self.name = name  # Attribute: Name of the dog
        self.age = age    # Attribute: Age of the dog

    # Method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

# Create an object (instance of the class)
my_dog = Dog("Buddy", 3)

# Access attributes and call methods
print(f"{my_dog.name} is {my_dog.age} years old.")  # Output: Buddy is 3 years old.
print(my_dog.bark())  # Output: Buddy says Woof!