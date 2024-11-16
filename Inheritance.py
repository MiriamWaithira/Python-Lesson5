# classes can inherit attributes and methods from other classes

# Imagine a Vehicle class with general features (like wheels).
# We can create subclasses like Car and Bike that inherit those features

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

car = Car(4)
bike = Bike(2)
print(car.wheels)  #Output: 4
print(bike.wheels)      #Output:2