# Object-Oriented Programming (OOP) in Python

This is a simple guide to understanding **Object-Oriented Programming (OOP)** in Python. OOP is a programming paradigm that uses **objects** and **classes** to structure code in a reusable and organized way.

---

## Key OOP Concepts

1. **Class**: A blueprint for creating objects. It defines properties (attributes) and behaviors (methods).
2. **Object**: An instance of a class. It contains data (attributes) and functions (methods).
3. **Encapsulation**: Bundling data and methods into a single unit (class) and controlling access to them.
4. **Inheritance**: Creating a new class (child class) from an existing class (parent class) to reuse and extend functionality.
5. **Polymorphism**: The ability to use a single interface for different data types or classes.

---

## Example Code

Here’s a simple Python example to demonstrate OOP:

### File: `main.py`

```python
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
```

---

## How to Run

1. Save the code in a file named `main.py`.
2. Open a terminal or command prompt.
3. Run the file using Python:
   ```bash
   python main.py
   ```

---

### Output

When you run the program, you will see the following output:

```
Buddy is 3 years old.
Buddy says Woof!
```

---

## Explanation

1. **Class Definition**: The `Dog` class is defined with a constructor (`__init__`) to initialize the `name` and `age` attributes.
2. **Object Creation**: An object `my_dog` is created from the `Dog` class with the name `"Buddy"` and age `3`.
3. **Accessing Attributes**: The `name` and `age` attributes of the object are accessed and printed.
4. **Calling Methods**: The `bark` method is called, which returns a string and is printed.

This is a basic introduction to OOP in Python. Happy coding! 🚀
