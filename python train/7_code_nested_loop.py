# # nested loops
# for outer_varialbe inouter_sequence:
#     for inner_variable in inner_sequence:
#         code block to execute for each combinatin of outer and inner variables


#basic nested loop
# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

for i in range(1,4):
    for j in range(1,4):
        print(i * j, end=" ")
    print()

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i = {i}, j = {j}")

for i in range(3):
    for j in range(3):
        if j == 1:
            continue # skip the curren iteration of the inner loop
        print(f"i = {i}, j = {j}")

#example:printing a triangle pattern

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=' ')
    print()

# flattening a 2d list using nested loops
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

flat_list = []
for row in matrix:
    print(row)
    for element in row:
        print(element)
        flat_list.append(element)
print(flat_list)


#using nested loops with dictinaries

students_scores = {
    "Alice" : [85,92,88],
    "Bob" : [78,81,79],
    "Charlie":[90,94,89]
}

for student, scores in students_scores.items():
    print(f"{student}'s scores {scores}")
    for score in scores:
        print(score)