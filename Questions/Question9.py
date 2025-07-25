# Fibonacci Series Between 0 and 50

num1, num2 = 0, 1
print("Fibonacci Series between 0 and 50:")

while num1 <= 50:
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2

print()