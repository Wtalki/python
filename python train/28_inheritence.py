# basic inheritance 

class Animal:
    def __init__(self,name):
        self.name = name #isntance varialb eofr the name of animal
        
    def eat(self):
        print(f"{self.name} is eating")

# define a chiild class name dog that ingerits for animal 
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says woof!")
        
dog = Dog("buddy")
dog.eat()
dog.bark


# super() function for accessing parent class 
class Animal:
    def __init__(self,name):
        self.name = name 
    
    def eat(self):
        print(f"{self.name} is eating")
        
class Dog(Animal):
    
    # initialize the parent class's attribues 
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):print(f"{self.name}, the {self.breed},says woof")
        
dog = Dog("buddy","golden retiver")
dog.eat()
dog.bark()


# 3 method overriding 
class Animal:
    def sound(self):
        print("some geeric animal sounc")
        
class Dog(Animal):
    def sound(self):
        print("wooof")
class Cat(Animal):
    def sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()   

dog.sound()
cat.sound()


# 4 multiple inheritance 
class Flyer:
    def fly(self):
        print("This hello can fly.")
    
class Swimmer:
    def swim(self):
        print("This object can swim")
        
class Duck(Flyer,Swimmer):
    def quack(self):
        print("Quack")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()


# 5 the isinstance and issubclass functions 
class Animal:
    pass
class Dog(Animal):
    pass
dog = Dog()

print(isinstance(dog,Dog))
print(isinstance(dog,Animal))

print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))


# inheritance with protected and private attributes 
class Animal:
    def __init__(self,name,age):
        self._age = age #protected attribute 
        self.__name = name#private attribue
        
    def get_name(self):
        return self.__name
class Dog(Animal):
    def display_info(self):
        print(f"age: {self._age}")
        print(f"name:{self.get_name()}")
        
dog = Dog("buddy",5)
dog.display_info()