# Creating the dictionary
cubes_dict = {x: x**3 for x in range(1, 6)}
print("Dictionary with cubes:", cubes_dict)


print("==================")


# Accessing and printing the student's name
student = {'name': 'John', 'age': 22, 'grade': 'A'}
print("Student's name:", student['name'])

# Updating the grade
student['grade'] = 'A+'
print("Updated dictionary:", student)



print("==================")


# Adding a new item
inventory = {'apples': 10, 'bananas': 5}
inventory['oranges'] = 7
print("After adding oranges:", inventory)

# Removing bananas
inventory.pop('bananas')
print("After removing bananas:", inventory)



print("==================")

# Checking key presence
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}
if 'David' in scores:
    print("'David' is in the dictionary.")
else:
    print("'David' is not in the dictionary.")


print("==================")


# Iterating through the dictionary
example_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key, value in example_dict.items():
    print(f"Key: {key}, Value: {value}")


print("==================")


# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}  # Alternatively: merged_dict = dict1 | dict2 (Python 3.9+)
print("Merged dictionary:", merged_dict)


