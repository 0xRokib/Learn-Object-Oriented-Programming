# Class, Static, and Instance Methods in Python

## Introduction

In Python, class methods, static methods, and instance methods define different behaviors and access levels within a class. Understanding their differences helps in writing clean and efficient object-oriented programs.

## Instance Method

An instance method is the most common type of method in a class. It operates on an instance of the class and can modify instance attributes.

### Syntax

```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"Instance method called. Name: {self.name}"

# Usage
obj = MyClass("Alice")
print(obj.instance_method())
```

### Key Points

- Defined without any decorator.
- First parameter is `self`, which refers to the instance.
- Can modify instance attributes.
- Can access both instance and class variables.

## Class Method

A class method is bound to the class rather than an instance. It can modify class state that applies across all instances.

### Syntax

```python
class MyClass:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        return f"Class method called. Class variable: {cls.class_variable}"

# Usage
print(MyClass.class_method())
```

### Key Points

- Defined using `@classmethod` decorator.
- First parameter is `cls`, representing the class itself.
- Can access and modify class variables but not instance variables.

## Static Method

A static method does not operate on an instance or class. It is simply a utility function inside a class.

### Syntax

```python
class MyClass:
    @staticmethod
    def static_method():
        return "Static method called. No access to class or instance attributes."

# Usage
print(MyClass.static_method())
```

### Key Points

- Defined using `@staticmethod` decorator.
- No `self` or `cls` parameter.
- Used for utility functions that don’t need class or instance data.

## Differences

| Feature                       | Instance Method                     | Class Method                    | Static Method                           |
| ----------------------------- | ----------------------------------- | ------------------------------- | --------------------------------------- |
| Decorator                     | None                                | `@classmethod`                  | `@staticmethod`                         |
| First Parameter               | `self` (instance itself)            | `cls` (class itself)            | No specific parameter                   |
| Access to Instance Variables  | Yes                                 | No                              | No                                      |
| Access to Class Variables     | Yes                                 | Yes                             | No                                      |
| Can Modify Instance Variables | Yes                                 | No                              | No                                      |
| Can Modify Class Variables    | No                                  | Yes                             | No                                      |
| Tied to an Instance           | Yes                                 | No                              | No                                      |
| Tied to a Class               | No                                  | Yes                             | No                                      |
| Use Case                      | Working with instance-specific data | Modifying class-wide attributes | Utility functions with no class context |

## When to Use

- **Instance Methods**: When you need to access or modify instance attributes.
- **Class Methods**: When you need to modify or access class attributes.
- **Static Methods**: When you need a function inside a class that doesn’t require class or instance data.

## Conclusion

Understanding instance, class, and static methods is crucial for writing organized and reusable object-oriented code. Each type serves a distinct purpose and should be used accordingly to maintain clean and maintainable code structures.
