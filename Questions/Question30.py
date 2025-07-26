with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

fruits = ["apple", "banana", "cherry"]
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

with open("data.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

with open("output.txt", "a") as file:
    file.write("Hello, World!\n")

with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
    for line in src:
        dest.write(line)
