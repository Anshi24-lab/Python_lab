num = []
for i in range(1,6):
    value = float(input(f"Enter number {i}:"))
    num.append(value)

sum = sum(num)
avg = sum / len(num)

print(f"The sum of the numbers is: {sum}")
print(f"The average of the numbers is: {avg}")
