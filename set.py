#Check if 'apple' is present in the set
fruits = {'apple', 'banana', 'cherry'}
if 'apple' in fruits:
    print("'apple' is present in the set.")
else:
    print("'apple' is not present in the set.")


print("==========================")


#Length of a set
numbers = {10, 20, 30, 40, 50}
print("The length of the set is:", len(numbers))


print("==========================")


#Remove duplicates from a list
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print("List after removing duplicates:", unique_list)


print("==========================")


#Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1).intersection(set(list2))
print("Common elements:", common_elements)


print("==========================")


#Unique characters in a string
string = "programming"
unique_characters = set(string)
print("Unique characters in the string:", unique_characters)


print("==========================")


#Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)


print("==========================")


#Intersection of sets
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
intersection_set = A.intersection(B)
print("Intersection of sets:", intersection_set)


print("==========================")


#Difference of sets
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
difference_set = X.difference(Y)
print("Difference of sets (X - Y):", difference_set)
