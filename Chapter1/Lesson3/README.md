# Lesson 3: Attributes and Methods in Python

This lesson focuses on **attributes** and **methods**, which are essential components of **Object-Oriented Programming (OOP)** in Python. Attributes store data, and methods define behaviors for objects. Understanding how to use them effectively is key to building robust and reusable code.

---

## Key Concepts

1. **Attributes**:

   - Variables that belong to an object or class.
   - Store data specific to the object (e.g., `name`, `age`).
   - Can be **instance attributes** (unique to each object) or **class attributes** (shared across all objects).

2. **Methods**:
   - Functions defined within a class.
   - Define behaviors or actions that an object can perform (e.g., `bark()`, `eat()`).
   - Can access and modify the object's attributes.

---

## Detailed Example: Attributes and Methods

Let’s create a detailed example to understand how attributes and methods work in Python.

### File: `main.py`

```python
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
```

---

## Explanation of the Code

1. **Class Definition**:

   - The `Dog` class is defined with a **class attribute** (`species`) and **instance attributes** (`name`, `age`, `breed`).

2. **Instance Attributes**:

   - Unique to each object (e.g., `dog1.name`, `dog2.age`).

3. **Instance Methods**:

   - `bark()`, `eat(food)`, and `sleep()` are methods that define behaviors for the objects.

4. **Class Attribute**:

   - `species` is a class attribute shared by all objects of the class.

5. **Object Creation**:

   - Two objects (`dog1` and `dog2`) are created from the `Dog` class.

6. **Accessing Attributes and Methods**:
   - Instance attributes and methods are accessed using dot notation.
   - Class attributes are accessed using the class name.

---

## How to Run

1. Save the code in a file named `main.py`.
2. Run the file using Python:
   ```bash
   python main.py
   ```

---

### Output

```
Buddy is a 3-year-old Golden Retriever.
Max is a 5-year-old German Shepherd.
Buddy says Woof!
Max is eating chicken.
Buddy is sleeping. Shhh!
Species: Canis familiaris
```

---

## Key Takeaways

- **Attributes** store data, and **methods** define behaviors.
- **Instance attributes** are unique to each object, while **class attributes** are shared across all objects.
- Use dot notation to access attributes and call methods.

---
