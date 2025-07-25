# Get Largest Number in List

# Write a Python program to get the largest number from a list.

list = [12,3,45,6]

l = list[1]

for i in list:
    if i > l:
        l = i

print(l)