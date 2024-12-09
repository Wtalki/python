# method overiding ofr ploymorphism 
# wrong way : not overiding the mehtod correctly 

class Dog:
    def sound(self):
        print("Woof!")

class Cat:
    def sound(self):
        print("Meow!")
    
def make_sound(animal):
    if isinstance(animal,Dog):
        animal.sound()
    else:
        print("Unknown animal")

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)



# right way using duck typeing 
class Dog:
    def sound(self):
        print("wooof")
        
class Cat:
    def sound(self):
        print("Meow!")

def make_sound(animal):
    animal.sound()
    
dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)


# polymorphism with colectins 

class Dog:
    def sound(self):
        print("woof")
        
class Cat:
    def sound(self):
        print("Meow!")

class Bird:
    def sound(self):
        print("Tweet!")

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.sound()