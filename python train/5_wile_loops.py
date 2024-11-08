# # while loops

# while condition:
#     code block to execute

# basic while loop example

count =0 
while count < 5:
    print(count)
    count += 1

# infinite while loop 
# while True:
#     print("this will print forever")

# while True:
#     name = input("what do you want to do")
#     print(name)
#     if name =='y':
#         break
        
# breaking the while loop with break 
while count < 10:
    print(count)
    if count == 5:
        break
    count += 1
    
# skippin an iteration with continue 

count = 0
while count < 5:
    count +=1
    if count == 3:
        continue # skip printing 3
    print(count)
    
# else with wile loop 

count = 0 
while count < 10:
    print(count)
    count += 1
else:
    print("loop finished")
    

count =0
while count < 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print("this will not print")
    
#pracitcal examples of while loops 

count = 5
while count > 0:
    print(count)
    count -= 1
else:
    print("blast off!")


# example 2:user input loop 
while True:
    user_input = input("enter 'exti to stop")
    if user_input =='exit':
        print("exition the loop")
        break
    else:
        print(f"yeou entered:{user_input}")

# summing numbers until a condition is met 
total = 0
while total < 100:
    number = int(input("Enter a number to add to the total: "))
    total += number
    print(f"Current total: {total}")
