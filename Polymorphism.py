class Car:
    def move(self):
        print("car drives.")

class Boat:
    def move(self):
        print("boat sails.")

class Plane:
    def move(self):
        print("plane flies.")

vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()
