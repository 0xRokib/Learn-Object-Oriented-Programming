import functools
# Method Decorators
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



# Class Method Decorators
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


# Property Decorators
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

# Class Decorators
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