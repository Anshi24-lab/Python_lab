numbers_divisible_by_5 = [x for x in range(1, 51) if x % 5 == 0]
print(numbers_divisible_by_5)

print("======================")

string = "comprehension"
vowels = [char for char in string if char in "aeiou"]
print(vowels)

print("======================")

primes = [x for x in range(2, 50) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)

print("======================")

'''numbers = [1, 2, 3, 4, 5]
factorials = [1 if num == 0 or num == 1 else num * [1 if i == 0 else i for i in range(1, num)][-1] for num in numbers]
print(factorials)'''


print("======================")


import math

numbers = [1, 2, 3, 4, 5]
factorials = [math.factorial(num) for num in numbers]
print(factorials)


print("======================")

'''numbers = [1, 2, 3, 4, 5]

factorials = [1 if x == 0 or x == 1 else 
              x * [1 for x in numbers]]

print(factorials)'''






