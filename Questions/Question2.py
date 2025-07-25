# Temp Converter 

# Formula = c/5 = f-32/9

print("Enter 1 for C to F")
print("enter 2 for F to C")

conv = input("Enter the value")

if (conv == 1):
    Cel_Val = int(input("enter the c value"))
    F = (Cel_Val/5) + (32/9)
    print(f"{Cel_Val}°C is {F}in Fahrenheit")
else:
    Fa_val = int(input("Enter the F cal"))
    C = 5 * (Fa_val - (32 / 9))
    print(f"{Fa_val}°F is {C} in Celsius")
