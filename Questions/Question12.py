# Get Largest Number in List

# Write a Python program to get the largest number from a list.

l_list = [12,3,45,6]

l = l_list[1]

for i in l_list:
    if i > l:
        l = i

print(l)