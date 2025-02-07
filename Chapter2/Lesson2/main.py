# Base Class: Vehicle

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
    


# Derived Classes
# 1. Car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk(self):
        return f"{self.make} {self.model} goes 'Beep Beep!'"

    def __str__(self):
        return f"{super().__str__()} | Doors: {self.num_doors}"
    
# 2. Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def load_cargo(self):
        return f"{self.make} {self.model} is loading {self.payload_capacity} kg of cargo."

    def __str__(self):
        return f"{super().__str__()} | Payload Capacity: {self.payload_capacity} kg"
    

# 3. Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        return f"{self.make} {self.model} is doing a wheelie!"

    def __str__(self):
        return f"{super().__str__()} | Sidecar: {'Yes' if self.has_sidecar else 'No'}"
    
    
# 4. ElectricCar
class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.make} {self.model} is charging with {self.battery_capacity} kWh battery."

    def __str__(self):
        return f"{super().__str__()} | Battery Capacity: {self.battery_capacity} kWh"
    
# Example Usage
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