# Base class
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    # Method that can be overridden
    def description(self):
        return f"{self.name} has a maximum speed of {self.max_speed} km/h."

# Subclass Car
class Car(Vehicle):
    def __init__(self, name, max_speed, doors):
        super().__init__(name, max_speed)
        self.doors = doors

    # Overriding method
    def description(self):
        return f"The car {self.name} with {self.doors} doors can reach {self.max_speed} km/h."

# Subclass Bike
class Bike(Vehicle):
    def __init__(self, name, max_speed, bike_type):
        super().__init__(name, max_speed)
        self.bike_type = bike_type

    # Overriding method
    def description(self):
        return f"The {self.bike_type} bike {self.name} can reach {self.max_speed} km/h."

# Testing the classes
vehicle = Vehicle("A generic Vehicle", 180)
car = Car("Toyota Auris", 220, 4)
bike = Bike("BMW S1000RR", 299, "sport")

print(vehicle.description())
print(car.description())
print(bike.description())

