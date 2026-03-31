class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        baseamount = super().fare()
        total = baseamount + (0.10 * baseamount)
        return total
    
SchoolBus = Bus ("School Volvo", 50)
print("The total bus fare is", SchoolBus.fare)