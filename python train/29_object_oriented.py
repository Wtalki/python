# OOp in python 


# 1. encapsulation 

class BankAccount:
    def __init__(self,owner,balance= 0):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} depoosited. new balance: ${self.__balance}")
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdawn. new balance:{self.__balance}")
        else:
            print("insufficient funds or invalid amount")
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount("zaw lay",100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())



# 2 abstraction 
from abc import ABC, abstractmethod 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(5,10)
print(rect.area())
print(rect.perimeter())
 
 
# 4 polymorphism 
class Animal:
    def sound(self):
        return "Some generic animal sounc"
class Dog(Animal):
    def sound(self):
        return "woof"
class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())
    
dog = Dog()
cat = Cat()

make_sound(dog) 
make_sound(cat)   

#classes and objects in oop 
class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"the {self.make}{self.model} is driving")

my_car = Car("Toyota","corolla")
my_car.drive()


from car import Car       
car1 = Car("hello",200,"yellow",True) 

car2 = [car1.model, car1.years, car1.color, car1.for_sale]
for i in car2:
    print(i)

car1.stop()
car1.drive()
# print(car1.model)
# print(car1.years)
# print(car1.color)
# print(car1.for_sale)
