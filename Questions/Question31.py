# 1. Read Entire File

# Write a Python program to read an entire text file.

# Click me to see the sample solution


with open("./Day0/notes.md", "r") as file:
    var = file.readlines()
    # print(var)



# 2. Read First N Lines

# Write a Python program to read first n lines of a file.

# Click me to see the sample solution

# with open("./Day0/notes.md", "r") as file:
#     var = file.readlines()
#     user = int(input("enter the number of lines : "))
#     for i in range(0,user):
#         print(var[i])

# 3. Append Text and Display

# Write a Python program to append text to a file and display the text.

# Click me to see the sample solution


# 4. Read Last N Lines

# Write a Python program to read last n lines of a file.

# Click me to see the sample solution

with open("./Day0/notes.md", "r") as file:
    var = file.readlines()
    user = int(input("enter the number of lines : "))
    for i in range(len(var) -1,len(var) - user,-1):
        print(var[i])


# 5. File to List

# Write a Python program to read a file line by line and store it into a list.

# Click me to see the sample solution

