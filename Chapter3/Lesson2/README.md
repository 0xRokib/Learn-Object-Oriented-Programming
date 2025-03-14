# Decorators in Object-Oriented Programming (OOP)

## Introduction

Decorators in Python provide a powerful way to modify the behavior of functions or methods without modifying their actual code. In Object-Oriented Programming (OOP), decorators can be particularly useful for method enhancements, access control, logging, memoization, and more.

## What Are Decorators?

A decorator is a higher-order function that takes another function (or method) as an argument and extends or alters its behavior without modifying it explicitly. Decorators use the `@decorator_function` syntax.

## Common Use Cases of Decorators in OOP

### 1. Method Decorators

Method decorators modify instance methods or class methods.

#### Example: Logging Decorator

```python
import functools

def log_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Method {func.__name__} returned: {result}")
        return result
    return wrapper

class ExampleClass:
    @log_method
    def greet(self, name):
        return f"Hello, {name}!"

obj = ExampleClass()
obj.greet("Alice")
```

### 2. Class Method Decorators

Decorators can also be applied to `@classmethod` and `@staticmethod`.

#### Example: Enforcing a Class-Level Constraint

```python
class MyClass:
    _instances = 0

    @classmethod
    def instance_count(cls):
        return cls._instances

    def __init__(self):
        MyClass._instances += 1

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.instance_count())  # Output: 2
```

### 3. Property Decorators

The `@property` decorator allows defining a method that behaves like an attribute.

#### Example: Read-Only Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.1416 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # Output: 5
print(circle.area)    # Output: 78.54
```

### 4. Class Decorators

Class decorators are applied at the class level to modify the behavior of the entire class.

#### Example: Singleton Pattern

```python
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Database connection established")

# Only one instance is created
db1 = Database()
db2 = Database()
print(db1 is db2)  # Output: True
```

## Conclusion

Decorators in OOP provide an elegant and reusable way to modify behavior without altering existing code. They can be used for logging, validation, enforcing constraints, and implementing design patterns like Singletons. Mastering decorators can significantly improve your Python OOP skills and make your code more modular and maintainable.
