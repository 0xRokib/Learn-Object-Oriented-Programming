# main.py
# A detailed example of attributes and methods in Python

# Step 1: Define a class
class Dog:
    # Step 2: Class attribute (shared by all objects)
    species = "Canis familiaris"

    # Step 3: Constructor (initializes instance attributes)
    def __init__(self, name, age, breed):
        # Instance attributes (unique to each object)
        self.name = name   # Name of the dog
        self.age = age     # Age of the dog
        self.breed = breed # Breed of the dog

    # Step 4: Instance method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

    # Step 5: Instance method (behavior)
    def eat(self, food):
        return f"{self.name} is eating {food}."

    # Step 6: Instance method (behavior)
    def sleep(self):
        return f"{self.name} is sleeping. Shhh!"

# Step 7: Create objects (instances of the class)
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 5, "German Shepherd")

# Step 8: Access instance attributes
print(f"{dog1.name} is a {dog1.age}-year-old {dog1.breed}.")  # Output: Buddy is a 3-year-old Golden Retriever.
print(f"{dog2.name} is a {dog2.age}-year-old {dog2.breed}.")  # Output: Max is a 5-year-old German Shepherd.

# Step 9: Call instance methods
print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.eat("chicken"))  # Output: Max is eating chicken.
print(dog1.sleep())  # Output: Buddy is sleeping. Shhh!

# Step 10: Access class attribute
print(f"Species: {Dog.species}")  # Output: Species: Canis familiaris