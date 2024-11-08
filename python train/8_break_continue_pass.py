# # break continue pass
# for/while loop:
#     if condition:
#         break continue pass

for number in range(1,6):
    if number == 3:
        break
    print(number) #output 1 2

count = 0
while count < 10:
    print(count)
    if count == 5:
        break
    count += 1

for number in range(1,6):
    if number == 3:
        continue
    print(number) #output 1 2 4 5

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count) #output 1 2 4 5

# pass 
for number in range(1,6):
    if number == 3: 
        pass #placeholder: dosen't affect the loop
    print(number)

