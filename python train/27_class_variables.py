# 1 class basic and instance variables 

#define a basic class name "Car"
class Car:
    #constructor method: called when a new instance is created
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer = 0 #initial odometer reading default is 0 miles
        
    # method to drive the car a creation number of mils 
    def drive(self,miles):
        self.odometer += miles
        print(f"{self.make} {self.model} has driven {miles} miles")
        
    #method to get current odomether reading
    def get_odomether(self):
        return self.odometer
    
my_car = Car("toyota","corolla",2002)

print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.drive(140)
print(my_car.get_odomether())


# 2 class variables 
class Carr:
    wheels = 4 # assuming all cars have 4 weels 
    def __init__(self,make,model):
        self.make = make
        self.model = model
        
car1 = Carr("toyota","corolla")
car2 = Carr("honda","civic")

print(car1.wheels)
print(car2.wheels)


# changing the class variable through the class itself 
Carr.wheels = 6
print(car1.wheels)
print(car2.wheels)

# 3. Differences Between Instance Variables and Class Variables
# Feature	Instance Variable	Class Variable
# Defined	Inside the __init__ method with self	Outside any method, no self
# Unique/Shared	Unique to each instance	Shared across all instances of the class
# Accessed by	self.instance_variable_name	ClassName.variable_name or self.variable_name
# Example Use	Attributes specific to each object (e.g., mileage)	Attributes common to all objects (e.g., wheels)


# 4 Accessing class and instance variables in mthods 
class Car:
    wheels = 4
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        #access class variable with self or Car.wheels
        print(f"wheels: {self.wheels}")
        
    @classmethod
    def set_wheels(cls,number):
        cls.wheels = number #modifies the class variable for all instances 

car1 = Car("toyota","corolla")
car2 = Car ("honda","civic")

car1.display_info()
Car.set_wheels(6)

car1.display_info()


# static variables and methods 
class MathOpeartions:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def multiply(x,y):
        return x * y
print(MathOpeartions.add(5,3))
print(MathOpeartions.multiply(4,6))
        
        
        