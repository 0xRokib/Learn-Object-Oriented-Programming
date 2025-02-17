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


# Example: Custom Iterable
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


# Example: Callable Object
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return self.factor * value

triple = Multiplier(3)
print(triple(10))  # Output: 30


# Example: Custom Context Manager
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
    
    
# Example: Overriding Equality
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