# Every time you create a new object, you want it to have its unique attributes (color, model, etc.)
# Constructors (__init__ methods) allow each object to start with specific values.

# Instance variables are specific to each object and can vary across objects
# For example, two Car objects can have different colors, models, and speeds

class Car:
    def __init__(self, color, model):
        self.color = color  #Instance variable
        self.model = model  #Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  #Output: blue
print(car2.model)  #Output: SUV