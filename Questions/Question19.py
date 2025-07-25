# 5. Factorial of a Number

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def Fact(n):
    ans = 1

    for i in range(n,0,-1):
        ans = ans * i

    return ans

print(Fact(5))