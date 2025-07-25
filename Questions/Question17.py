# 2. Sum All Numbers in a List

# Write a Python function to sum all the numbers in a l_list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def funct(l_list):
    ans = 0
    for i in l_list:
        ans = ans + i
    
    return ans
print(funct([8, 2, 3, 0, 7]))