# Instance Method
class MyClass:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"Instance method called. Name: {self.name}"

# Usage example
obj = MyClass("Alice")
print(obj.instance_method())

#Class Method
class MyClass:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        return f"Class method called. Class variable: {cls.class_variable}"

# Usage
print(MyClass.class_method())


# Static Method 
class MyClass:
    @staticmethod
    def static_method():
        return "Static method called. No access to class or instance attributes."

# Usage
print(MyClass.static_method())
