#  Inheritance

# Inheritance is a fundamental concept in object-oriented programming (OOP) that involves creating new classes (subclasses or derived classes) based on existing classes(superclasses or base classes)

# - A Car is-a Vehicle
# - A Bike is-a Vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")
        
class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        # super() call the attributes of the Vehicle's superclass for the Car subclass
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels
        
class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        # super() call the attributes of the Vehicle's superclass for the Bike subclass
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
        
car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "Scoopy", 2018, 2)
print(car.__dict__)
car.start()
print(bike.__dict__)
bike.start()
