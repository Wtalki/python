# file direction 
# file = open("example.txt", "r")
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "r") as file:
#     line = file.readline()  # Reads the first line
#     print(line)

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # Print each line without extra newline


# with open("hello.txt",'w') as file:
#     file.write("hello, world\n")

# lines = ["line 1\n",'line 2\n','line 3\n']
# with open("hellow.txt",'w') as file:
#     file.writelines(lines) 

# with open("example.txt", "a") as file:
#     file.write("this will be appended to the file. \n")   

# filename = "data.txt"

# with open(filename, "w") as file:
#     file.write("python is great for file operatinons\n")
#     file.write("this is another line.\n")
    
# with open(filename,"a") as file:
#     file.write("appending a new line here.\n")
    
# with open(filename,"r") as file:
#     print("file contents:")
#     print(file.read())


# with open("example.txt","r") as file:
#     file.seek(5)
#     content = file.read()
#     print(content)
    
# with open("example.txt", "r") as file:
#     file.read(5)
#     position = file.tell()
#     print("file pointer is a byte:", position)
    
import os
# os.remove("example.txt")

# if os.path.exists("example.txt"):
#     print("file exitsts.")
# else:
#     print("file does not exist")

with open("image.png", "rb") as file:
    binary_data = file.read()
    print(binary_data)
    