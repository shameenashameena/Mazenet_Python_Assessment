# Exercise 9: OOP – Class and Inheritance

# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


# Subclass
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  
        self.num_doors = num_doors

    # Method to display attributes
    def display_info(self):
        print(
             f"Make: {self.make}, "
             f"Model: {self.model}, "
             f"Number of Doors: {self.num_doors}"
        )
          
          
my_car = Car("Toyota", "Corolla", 4)
my_car.display_info()

