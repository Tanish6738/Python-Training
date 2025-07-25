# Pattern Printing

"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

num = int(input("enter the number"))


for i in range(1 ,num+1):
    print(" * " * i)
for i in range(num-1,0,-1):
    print(" * " * i)
   