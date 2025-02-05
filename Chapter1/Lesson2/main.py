# main.py
# Example of classes and objects in Python

# Define a class
class Dog:
    # Constructor (initializes attributes)
    def __init__(self, name, age):
        self.name = name  # Attribute: Name of the dog
        self.age = age    # Attribute: Age of the dog

    # Method: Simulate the dog barking
    def bark(self):
        return f"{self.name} says Woof!"

    # Method: Display dog information
    def display_info(self):
        return f"{self.name} is {self.age} years old."

# Create objects (instances of the class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Access attributes and call methods
print(dog1.display_info())  # Output: Buddy is 3 years old.
print(dog1.bark())          # Output: Buddy says Woof!

print(dog2.display_info())  # Output: Max is 5 years old.
print(dog2.bark())          # Output: Max says Woof!