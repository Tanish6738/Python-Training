# Print Items with Types 


datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for i in datalist:
    print(f"{i} is of Data type {type(i)}" ,end="\n\n")