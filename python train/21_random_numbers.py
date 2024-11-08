import random 
random_float = random.random()
print(random_float)

random_int = random.randint(1,10)
print(random_int)

random_float = random.uniform(5.5,9.5)
print(random_float)

random_step = random.randrange(0,100,10)
print(random_step)

options = ["apple","banana","cherry"]
random_choices = random.choices(options,k=3)
print(random_choices)

random_choices = random.choices(options,weights=[5,1,1,], k= 5)
print(random_choices)

options = ["apple","banana","cherry","date"]
random_sample = random.sample(options,k=2)
print(random_sample)

numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)

random.seed(42)
print(random.randint(1,10))
print(random.random())

import random
import string 
 
def generate_passwrod(length = 8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k = length))
    return password

password = generate_passwrod(12)

print(password)
    