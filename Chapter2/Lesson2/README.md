# Python Inheritance: Types and Real-World Example

This repository explains the **types of inheritance** in Python and demonstrates their application using a **real-world example** of a **vehicle management system**. Inheritance is a key concept in object-oriented programming (OOP) that allows classes to inherit attributes and methods from other classes, promoting code reusability, organization, and extensibility.

---

## Types of Inheritance

Python supports several types of inheritance. Below are examples of each type using a **vehicle management system** as the context.

### 1. **Single Inheritance**

A child class inherits from a single parent class.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting."

class Car(Vehicle):  # Single inheritance
    def honk(self):
        return f"{self.make} {self.model} goes 'Beep Beep!'"

# Usage
car = Car("Toyota", "Corolla", 2022)
print(car.start())  # Output: Toyota Corolla is starting.
print(car.honk())   # Output: Toyota Corolla goes 'Beep Beep!'
```

---

### 2. **Multiple Inheritance**

A child class inherits from multiple parent classes.

```python
class Engine:
    def start_engine(self):
        return "Engine started."

class ElectricMotor:
    def charge_battery(self):
        return "Battery charging."

class HybridCar(Vehicle, Engine, ElectricMotor):  # Multiple inheritance
    pass

# Usage
hybrid_car = HybridCar("Toyota", "Prius", 2023)
print(hybrid_car.start())        # Output: Toyota Prius is starting.
print(hybrid_car.start_engine()) # Output: Engine started.
print(hybrid_car.charge_battery()) # Output: Battery charging.
```

---

### 3. **Multilevel Inheritance**

A child class inherits from a parent class, which in turn inherits from another class.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting."

class Car(Vehicle):  # First level of inheritance
    def honk(self):
        return f"{self.make} {self.model} goes 'Beep Beep!'"

class ElectricCar(Car):  # Second level of inheritance
    def charge(self):
        return f"{self.make} {self.model} is charging."

# Usage
electric_car = ElectricCar("Tesla", "Model S", 2023)
print(electric_car.start())  # Output: Tesla Model S is starting.
print(electric_car.honk())   # Output: Tesla Model S goes 'Beep Beep!'
print(electric_car.charge()) # Output: Tesla Model S is charging.
```

---

### 4. **Hierarchical Inheritance**

Multiple child classes inherit from a single parent class.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting."

class Car(Vehicle):  # Child class 1
    def honk(self):
        return f"{self.make} {self.model} goes 'Beep Beep!'"

class Truck(Vehicle):  # Child class 2
    def load_cargo(self):
        return f"{self.make} {self.model} is loading cargo."

# Usage
car = Car("Toyota", "Corolla", 2022)
truck = Truck("Ford", "F-150", 2020)

print(car.start())      # Output: Toyota Corolla is starting.
print(car.honk())       # Output: Toyota Corolla goes 'Beep Beep!'
print(truck.start())    # Output: Ford F-150 is starting.
print(truck.load_cargo())  # Output: Ford F-150 is loading cargo.
```

---

### 5. **Hybrid Inheritance**

A combination of two or more types of inheritance.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} is starting."

class Engine:
    def start_engine(self):
        return "Engine started."

class ElectricCar(Vehicle, Engine):  # Multiple inheritance
    def charge(self):
        return f"{self.make} {self.model} is charging."

class SelfDrivingCar(ElectricCar):  # Multilevel inheritance
    def drive_autonomously(self):
        return f"{self.make} {self.model} is driving autonomously."

# Usage
self_driving_car = SelfDrivingCar("Tesla", "Model X", 2024)
print(self_driving_car.start())           # Output: Tesla Model X is starting.
print(self_driving_car.start_engine())    # Output: Engine started.
print(self_driving_car.charge())          # Output: Tesla Model X is charging.
print(self_driving_car.drive_autonomously())  # Output: Tesla Model X is driving autonomously.
```

---

## Real-World Example: Vehicle Management System

Let’s apply these concepts to a real-world scenario where we manage a fleet of vehicles. Each vehicle type shares common properties (e.g., `make`, `model`, `year`) but has unique features.

### Base Class: `Vehicle`

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"{self.make} {self.model} (Year: {self.year}) is starting."

    def stop(self):
        return f"{self.make} {self.model} (Year: {self.year}) is stopping."

    def __str__(self):
        return f"{self.make} {self.model} (Year: {self.year})"
```

### Derived Classes

#### 1. `Car`

```python
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        return f"{self.make} {self.model} goes 'Beep Beep!'"

    def __str__(self):
        return f"{super().__str__()} | Doors: {self.num_doors}"
```

#### 2. `Truck`

```python
class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def load_cargo(self):
        return f"{self.make} {self.model} is loading {self.payload_capacity} kg of cargo."

    def __str__(self):
        return f"{super().__str__()} | Payload Capacity: {self.payload_capacity} kg"
```

#### 3. `Motorcycle`

```python
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        return f"{self.make} {self.model} is doing a wheelie!"

    def __str__(self):
        return f"{super().__str__()} | Sidecar: {'Yes' if self.has_sidecar else 'No'}"
```

#### 4. `ElectricCar`

```python
class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.make} {self.model} is charging with {self.battery_capacity} kWh battery."

    def __str__(self):
        return f"{super().__str__()} | Battery Capacity: {self.battery_capacity} kWh"
```

---

## Example Usage

```python
# Create instances
car = Car("Toyota", "Corolla", 2022, 4)
truck = Truck("Ford", "F-150", 2020, 1000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021, False)
electric_car = ElectricCar("Tesla", "Model S", 2023, 4, 100)

# Display vehicle details
print(car)          # Output: Toyota Corolla (Year: 2022) | Doors: 4
print(truck)        # Output: Ford F-150 (Year: 2020) | Payload Capacity: 1000 kg
print(motorcycle)   # Output: Harley-Davidson Sportster (Year: 2021) | Sidecar: No
print(electric_car) # Output: Tesla Model S (Year: 2023) | Doors: 4 | Battery Capacity: 100 kWh

# Use inherited methods
print(car.start())  # Output: Toyota Corolla (Year: 2022) is starting.
print(truck.stop()) # Output: Ford F-150 (Year: 2020) is stopping.

# Use unique methods
print(car.honk())           # Output: Toyota Corolla goes 'Beep Beep!'
print(truck.load_cargo())   # Output: Ford F-150 is loading 1000 kg of cargo.
print(motorcycle.wheelie()) # Output: Harley-Davidson Sportster is doing a wheelie!
print(electric_car.charge()) # Output: Tesla Model S is charging with 100 kWh battery.
```

---

## Key Concepts in This Example

1. **Inheritance**: Child classes (`Car`, `Truck`, `Motorcycle`, `ElectricCar`) inherit common properties and methods from the `Vehicle` class.
2. **Method Overriding**: Child classes can override methods from the parent class (e.g., `__str__`).
3. **`super()` Function**: Used to call the parent class's `__init__` method and initialize inherited attributes.
4. **Code Reusability**: Common functionality is defined once in the parent class and reused in child classes.
5. **Extensibility**: New vehicle types can be added easily without modifying existing code.

---

## The `__str__` Method

The `__str__` method is a special method in Python that defines how an object should be represented as a string. It is called when you use the `print()` function or the `str()` function on an object.

### Example:

```python
def __str__(self):
    return f"{self.make} {self.model} (Year: {self.year})"
```

### How It Works:

- When you call `print(object)`, Python internally calls `object.__str__()`.
- The `__str__` method returns a string that represents the object in a human-readable format.
- If `__str__` is not defined, Python falls back to the `__repr__` method.

### Why Use `__str__`?

- **Readability**: Provides a clear and concise way to display object details.
- **Customization**: Tailors the string representation to include only the most relevant information.
- **Debugging**: Makes it easier to inspect objects during development.

---

## Why Use Inheritance?

- **Reusability**: Avoid duplicating code by defining common functionality in a base class.
- **Organization**: Create a logical hierarchy of classes that reflect real-world relationships.
- **Extensibility**: Easily add new types of vehicles or features without modifying existing code.
- **Maintainability**: Changes to the base class automatically propagate to all derived classes.

This example demonstrates how inheritance can be applied to model real-world systems effectively. Happy coding! 🚗🚚🏍️
