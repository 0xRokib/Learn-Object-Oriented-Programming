# Lesson 2: Classes and Objects in Python

This lesson focuses on **classes** and **objects**, the foundation of **Object-Oriented Programming (OOP)** in Python. A **class** is a blueprint for creating objects, and an **object** is an instance of a class that contains data (attributes) and behaviors (methods).

---

## Key Concepts

1. **Class**: A blueprint that defines attributes and methods.
2. **Object**: An instance of a class with its own unique data.
3. **Attributes**: Variables that store data (e.g., `name`, `age`).
4. **Methods**: Functions that define behaviors (e.g., `bark()`, `eat()`).

---

## Example: Classes and Objects

### File: `main.py`

```python
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
```

---

## Explanation

1. **Class Definition**:

   - The `Dog` class is defined with a constructor (`__init__`) to initialize `name` and `age`.
   - Two methods are added: `bark()` and `display_info()`.

2. **Object Creation**:

   - Two objects (`dog1` and `dog2`) are created from the `Dog` class.

3. **Accessing Attributes and Methods**:
   - Attributes (`name`, `age`) are accessed using dot notation.
   - Methods (`bark()`, `display_info()`) are called using dot notation.

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
Buddy is 3 years old.
Buddy says Woof!
Max is 5 years old.
Max says Woof!
```

---

This lesson focuses on **classes** and **objects**. In the next lesson, we’ll dive deeper into **attributes** and **methods**. 🚀
