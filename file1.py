num = 1  
rows = 4  

for i in range(1, rows + 1): 
    for j in range(1, i + 1): 
        print(num, end=" ")  # Print the current number with a space
        num += 1  # Increment the number
    print()

print("==============")

rows = 5


for i in range(rows, 0, -1): 
    print(" " * (rows - i), end="")  
    for j in range(i, 0, -1):  
        print(j, end=" ")  
    print()  


print("===============")

rows = 5

for i in range(rows, 0, -1):  
    for j in range(1, i + 1):  
        print(j, end=" ")  
    print()  


print("================")

rows = 6


for i in range(1, rows + 1):  
    for j in range(i):  
        print(chr(65 + j), end=" ")  
    print() 


print("===============")

rows = 5

for i in range(1, rows + 1): 
    print(" " * (rows - i), end="")
    print("*" * (2 * i - 1))

    
