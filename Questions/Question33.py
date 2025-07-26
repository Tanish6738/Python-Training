
# 1. Handle ZeroDivisionError Exception

# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Click me to see the sample solution

# try :
#     a = int(input("Enter a : "))
#     b = int(input("Enter b : "))

#     ans = a / b 
#     print(ans)
# except Exception as e:
#     print(e)
# finally :
#     print("Me to chalunga")



# 2. Validate Integer Input and Raise ValueError

# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Click me to see the sample solution

# def new(string):
    
#     print(len(string))

# try :
#     new(45)
# except Exception as e :
#     raise ValueError
# finally :
#     print("Me to chalunga")



# 3. Handle FileNotFoundError Exception When Opening a File

# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

# Click me to see the sample solution

# try :
#     with open("new file ")as file:
#         print(file.read())
# except Exception as e:
#     print("Error  hai Bhai ")
#     raise FileNotFoundError



# 4. Validate Numerical Inputs and Raise TypeError

# Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

# Click me to see the sample solution

# try :
#     user = int(input("Enter are number only "))
#     print(user)
# except Exception as e :
#     print("Number Dal bas or kuch nahi")
#     raise TypeError
    


# 5. Handle PermissionError Exception When Opening a File

# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

# Click me to see the sample solution

# try :
#     with open("file.txt", "r") as file:
#         print(file.read())
# except Exception as e:
#     print("Error  hai Bhai ")
#     raise PermissionError