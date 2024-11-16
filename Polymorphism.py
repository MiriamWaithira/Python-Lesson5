# Derived classes can behave differently for the same method inherited from a base class
# With polymorphism, a method name can mean different things across multiple classes

# The speak method for dogs is bark while for cats is meow
# EXAMPLE 1
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

# Polymorphism in Action
for animal in [Dog(), Cat()]:
    print(animal.speak())


# EXAMPLE 2
class Luxury:
    def location(self):
        return "German"

class Reliability:
    def location(self):
        return "Asian"

# Polymorphism in Action
for function in [Luxury(), Reliability()]:
    print(function.location())