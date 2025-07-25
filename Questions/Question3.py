#number guessing game 

import random

num = random.randint(1, 9)
print(num)
choice = int(input("enter the num"))
while(num != choice):
    if (num < choice):
        print(f"too Large")
        choice = int(input("enter the num"))
    else :
        print("too small")
        choice = int(input("enter the num"))
else :
    print("you won")