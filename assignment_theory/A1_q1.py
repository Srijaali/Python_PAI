# Zoo Management System

# You are tasked with designing a Zoo Management System that handles
# various types of animals: Mammals,
# Birds, and Reptiles. Each type of animal has
# common attributes such as name, age, and habitat, but also has unique attributes:
# Mammals have a fur
# length and a diet type
# (e.g., herbivore, carnivore).
# Birds have a wingspan
# and a flight altitude.
# Reptiles have a scale
# pattern and a venomous
# status (e.g., venomous, non-venomous).
# The system should also track whether
# each animal is currently available
# for viewing or in quarantine.

# Requirements:
# Create a base class called Animal that encapsulates common attributes and methods.
# Implement subclasses for Mammal, Bird, and Reptile that inherit from Animal. Each subclass should have its unique attributes and
# methods.
# Add a method to mark an animal as available for viewing or in quarantine.
# Demonstrate polymorphism by implementing a method that displays information
# about each animal, which should be overridden in each subclass to show the
# unique details of that type.
# Provide code examples demonstrating the functionality of your classes,
# including creating instances and changing their availability status.

class Animal:
    def __init__(self,name,age,habitat):
        self.name=name
        self.age=age
        self.habitat=habitat
        self.available = True
    
    def display(self):
        status = "Available" if self.available else "in Quarantine"
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Habitat: {self.habitat}")
        print(f"Status: {status}")

    def set_availability(self, is_available):
        self.available = is_available

class Mammal(Animal):
    def __init__(self, name, age, habitat,fur_length,diet_type):
        super().__init__(name, age, habitat)
        self.fur_length=fur_length
        self.diet_type=diet_type

    def display(self):
       super().display()
       print(f"Fur Length: {self.fur_length}")
       print(f"Diet Type: {self.diet_type}")
    

class Bird(Animal):
    def __init__(self, name, age, habitat,wingspan,flight_altitude):
        super().__init__(name, age, habitat)
        self.wingspan=wingspan
        self.flight_altitude = flight_altitude

    def display(self):
        super().display()
        print(f"Wing-Span: {self.wingspan}")
        print(f"Flight Altitude: {self.flight_altitude}")

class Reptile(Animal):
    def __init__(self, name, age, habitat,scale_pattern):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous_status = True

    def display(self):
        super().display()
        print(f"Scale Pattern: {self.scale_pattern}")
        venom = "VENOMOUS" if self.venomous_status else "NON VENOMOUS"
        print(f"Venom: {venom}")
    

print("\n Mammal's Data: ")
m = Mammal("Cat",5,"Shelter house" , 125 , "Non-Veg")
m.display()
m.set_availability(False)
print("\n Updated Mammal's Availaility: ")
m.display()

print("\n BIRD's Data: ")
b = Bird("Sparrow" , 2 , "Nest" , 45 , 100)
b.display()
b.set_availability(True)
print("\n Updated Mammal's Availaility: ")
b.display()
print("\n Reptile's Data: ")
r = Reptile("Snake" , 23 , "Jungle" , "Zig-zag")
r.display()
r.set_availability(False)
print("\n Updated Mammal's Availaility: ")
r.display()


