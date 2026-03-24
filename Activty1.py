class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class Bus(Vehicle):
    pass

schoolbus = Bus("Avika", 200, 12)

print("The name of this school bus is", schoolbus.name)
print("The maximum speed of the school bus is", schoolbus.maxspeed)
print("The mileage of the school bus is", schoolbus.mileage)