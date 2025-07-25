# 6. Check if a Number Falls Within a Given Range

# Write a Python function to check whether a number falls within a given range.


def Falls(n, r):
    if n in range(r[0], r[1]+1):
        print("Yes")
    else :
        print("No")

Falls(2,[0,5])