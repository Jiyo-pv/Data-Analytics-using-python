# Q18 Inheritance and method overriding - @JIYO P V 2026-07-13
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, seating_capacity):
        super().__init__(brand, model)
        self.seating_capacity = seating_capacity

    def display_info(self):
        super().display_info()
        print("Seating Capacity:", self.seating_capacity)


v = Vehicle("Yamaha", "R15")
c = Car("Toyota", "Innova", 7)
print("Vehicle info:")
v.display_info()
print("Car info:")
c.display_info()
