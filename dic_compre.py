# Squares of numbers
squares_dict = {x: x**2 for x in range(1, 11)}
print("Squares of numbers:", squares_dict)


print("==================")


# Filter even numbers
even_squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Squares of even numbers:", even_squares_dict)


print("==================")


# Reverse dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original_dict.items()}
print("Reversed dictionary:", reversed_dict)


print("==================")


# Character frequency
string = "programming"
char_frequency = {char: string.count(char) for char in string}
print("Character frequency:", char_frequency)


print("==================")


# Nested dictionary
nested_dict = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}
print("Nested dictionary:", nested_dict)


print("==================")


# Zip two lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
zipped_dict = {k: v for k, v in zip(keys, values)}
print("Zipped dictionary:", zipped_dict)


print("==================")


# Filter dictionary by value
marks = {'Alice': 85, 'Bob': 65, 'Charlie': 90, 'David': 72}
filtered_marks = {k: v for k, v in marks.items() if v > 80}
print("Filtered dictionary:", filtered_marks)


print("==================")


# Multiplication table for 5
multiplication_table = {x: 5 * x for x in range(1, 11)}
print("Multiplication table for 5:", multiplication_table)


print("==================")


# Convert list to dictionary
data = [('a', 10), ('b', 20), ('c', 30)]
converted_dict = {k: v for k, v in data}
print("Converted dictionary:", converted_dict)

