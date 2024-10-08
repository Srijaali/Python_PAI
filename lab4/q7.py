# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10%
# on full fare as a maintenance charge. So total fare for bus instance will become the final
# amount = total fare + 10% of the total fare. 

class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
        
    def fare(self):
        return self.seating_capacity*100
    
class Bus(Vehicle):
    def fare(self):
        t_fare = super().fare() 
        final_fare = t_fare + (t_fare*0.10)
        return final_fare
    
vehicle = Vehicle(5)
print(f"fare of the vehicle is ${vehicle.fare()}")
bus = Bus(50)
print(f"the fare of the bus is ${bus.fare()}")
