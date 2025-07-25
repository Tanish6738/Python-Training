# Number of even and odds

even = 0
odd = 0

num = int(input("enter the Range"))

for i in range(num+1):
    if i % 2 == 0:
        even += 1
    else :
        odd += 1

print(f"Number of even {even} and Number of odds {odd}")