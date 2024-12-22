# Single Inheritance
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

car = Car()
car.move()  

#----------------------------------
# Multiple Inheritance
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Flyer:
    def fly(self):
        print("This vehicle can fly.")

class Plane(Vehicle, Flyer):
    def move(self):
        print("The plane flies in the sky.")

plane = Plane()
plane.move()  
plane.fly()   

#-------------------------------
# Multilevel Inheritance
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

class SportsCar(Car):
    def move(self):
        print("The sports car drives very fast on the road.")

sports_car = SportsCar()
sports_car.move()  

#--------------------
# Hierarchical Inheritance
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")

class Boat(Vehicle):
    def move(self):
        print("The boat sails on the water.")

car = Car()
boat = Boat()
car.move()   
boat.move()  

#-------------------------------
#  Hybrid Inheritance
class Vehicle:
    def move(self):
        print("This vehicle moves.")

class LandVehicle(Vehicle):
    def move(self):
        print("This land vehicle moves on the road.")

class WaterVehicle(Vehicle):
    def move(self):
        print("This water vehicle moves on water.")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def move(self):
        print("This amphibious vehicle moves on both land and water.")

amphibious = AmphibiousVehicle()
amphibious.move()  

