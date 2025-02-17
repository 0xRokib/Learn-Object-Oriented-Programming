# Python Magic Methods

## Introduction

Magic methods, also known as dunder (double underscore) methods, are special methods in Python that allow objects to interact with built-in functions and operators. These methods have names that start and end with double underscores (e.g., `__init__`, `__str__`). They enable operator overloading and customize object behavior.

## Common Magic Methods

### 1. Object Initialization & Representation

| Method                | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `__init__(self, ...)` | Constructor method; initializes an instance.                 |
| `__new__(cls, ...)`   | Creates a new instance of a class.                           |
| `__repr__(self)`      | Returns an official string representation of the object.     |
| `__str__(self)`       | Returns a user-friendly string representation of the object. |

### 2. Arithmetic Operations

| Method                      | Description                       |
| --------------------------- | --------------------------------- |
| `__add__(self, other)`      | Implements addition (`+`).        |
| `__sub__(self, other)`      | Implements subtraction (`-`).     |
| `__mul__(self, other)`      | Implements multiplication (`*`).  |
| `__truediv__(self, other)`  | Implements division (`/`).        |
| `__floordiv__(self, other)` | Implements floor division (`//`). |
| `__mod__(self, other)`      | Implements modulo (`%`).          |
| `__pow__(self, other)`      | Implements exponentiation (`**`). |

### 3. Comparison Operators

| Method                | Description                                 |
| --------------------- | ------------------------------------------- |
| `__eq__(self, other)` | Implements equality (`==`).                 |
| `__ne__(self, other)` | Implements inequality (`!=`).               |
| `__lt__(self, other)` | Implements less than (`<`).                 |
| `__le__(self, other)` | Implements less than or equal to (`<=`).    |
| `__gt__(self, other)` | Implements greater than (`>`).              |
| `__ge__(self, other)` | Implements greater than or equal to (`>=`). |

### 4. Container & Sequence Methods

| Method                          | Description                               |
| ------------------------------- | ----------------------------------------- |
| `__len__(self)`                 | Returns the length of the object.         |
| `__getitem__(self, key)`        | Retrieves an item using `obj[key]`.       |
| `__setitem__(self, key, value)` | Assigns a value using `obj[key] = value`. |
| `__delitem__(self, key)`        | Deletes an item using `del obj[key]`.     |
| `__iter__(self)`                | Returns an iterator object.               |
| `__next__(self)`                | Retrieves the next item in an iteration.  |

### 5. Attribute Access & Management

| Method                           | Description                                     |
| -------------------------------- | ----------------------------------------------- |
| `__getattr__(self, name)`        | Called when accessing a non-existent attribute. |
| `__setattr__(self, name, value)` | Called when setting an attribute.               |
| `__delattr__(self, name)`        | Called when deleting an attribute.              |

### 6. Callable & Context Management

| Method                                           | Description                                    |
| ------------------------------------------------ | ---------------------------------------------- |
| `__call__(self, ...)`                            | Allows an instance to be called as a function. |
| `__enter__(self)`                                | Used in context managers (`with` statement).   |
| `__exit__(self, exc_type, exc_value, traceback)` | Handles exit from a `with` block.              |

## Example Usage

```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return CustomNumber(self.value + other.value)

    def __str__(self):
        return f"CustomNumber({self.value})"

num1 = CustomNumber(10)
num2 = CustomNumber(20)
result = num1 + num2
print(result)  # Output: CustomNumber(30)
```

### Example: Custom Iterable

```python
class CustomList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

my_list = CustomList([1, 2, 3, 4])
print(my_list[2])  # Output: 3
print(len(my_list))  # Output: 4
```

### Example: Callable Object

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

triple = Multiplier(3)
print(triple(10))  # Output: 30
```

### Example: Custom Context Manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```

### Example: Overriding Equality

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("Alice", 25)
p2 = Person("Alice", 25)
p3 = Person("Bob", 30)

print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False
```

## Conclusion

Magic methods provide powerful customization of class behavior, enabling intuitive object interactions with Python's built-in functions and operators. By leveraging these methods, developers can create more expressive and flexible classes.
