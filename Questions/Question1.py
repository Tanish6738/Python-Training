# Divisible by 7 and multiple of 5 

n = int(input("enter the number"))

if ( n % 7 == 0 ):
    if (n % 5 == 0 ):
        print(True)
    else :
        print(False)
else :
    print(False)
