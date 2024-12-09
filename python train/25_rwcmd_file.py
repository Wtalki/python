# with open("zaw.txt",'w') as file:
#     file.write("hello world\n")
#     file.write("this is a new line")

# with open("zaw.txt", 'a') as file:
#     file.write("\nappending a new line")
    
    
# # writin multiple lines 
# lines = ["line 1\n", "line 2\n", "line 3\n", "line 4\n"]
# with open("zaw.txt",'w') as file:
#     file.writelines(lines)
    
# #copyint files 
# import shutil
# shutil.copyfile("zaw.txt","zaw_copy.txt")

# shutil.copyfile("zaw.txt","zawzaw.txt")

# #moving files
# shutil.move("zaw_copy.txt","python train/zaw_copy.txt")


# # deleting file 
# import os
# if os.path.exists('zawzaw.txt'):
#     os.remove("zawzaw.txt")
# else:
#     print("the file does not exist")


# # deletin a directory and its contents 
# import shutil
# shutil.rmtree("hello")


# example of file operations 
import os 
import shutil 


with open("example.txt", "w") as file:
    file.write ("hello world \n this is test fiel")
    
shutil.copy("example.txt", "example_copy.txt")

if  not os.path.exists("backup"):
    os.makedirs("backup")
    shutil.move("example_copy.txt", "backup/example_copy.txt")
    
if os.path.exists("example.txt"):
    os.remove("example.txt")
shutil.rmtree("backup")