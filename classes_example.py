class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.pasengers = []

    def add_pasenger(self,name):
        if not self.get_capacity():
            return False        
        self.pasengers.append(name)
        return True

    def get_capacity(self):
        return self.capacity - len(self.pasengers)

    
names = ["Harry", "Drako", "Harmionie", "Ron", "Ginni"]

flight = Flight(3)
for name in names:
    if(flight.add_pasenger(name)):
        print(f"Added {name} to flight successfully");
    else:
        print(f"No available seats for {name}.")