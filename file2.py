my_list = [10, 20, 30, 40, 50]


first_element = my_list[0]
print("First element:", first_element)


last_element = my_list[-1]
print("Last element using negative indexing:", last_element)


third_element = my_list[2]
print("Third element:", third_element)

print("=====================")

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print("Second element:", fruits[1])
print("Fourth element:", fruits[3])

fruits[2] = "Coconut"
print("Updated list:", fruits)

print("=====================")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first_five = nums[:5]
print("First 5 elements:", first_five)


alternate_elements = nums[1::2]
print("Every alternate element starting from the second element:", alternate_elements)


reversed_list = nums[::-1]
print("Reversed list:", reversed_list)

print("=====================")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

first_five_letters = alphabet[:5]
print("First 5 letters:", first_five_letters)


last_five_letters = alphabet[-5:]
print("Last 5 letters:", last_five_letters)


every_second_letter = alphabet[::2]
print("Every second letter:", every_second_letter)

print("=====================")

colors = ['red', 'blue','green']

print(colors)

colors.insert(1,'yellow')
colors.append('purple')
colors.insert(0,'orange')

print(colors)


print("=====================")

my_list = []

for num in range(1, 6):
    my_list.insert(0, num)  # insert at the beginning
print("List after inserting numbers 1 to 5 at the beginning:", my_list)

# insert the string 'middle' at index 2
my_list.insert(2, 'middle')
print("List after inserting 'middle' at index 2:", my_list)


print("=====================")


nums = [10, 20, 30, 40, 50, 60]

nums.pop(2)
print("After removing the third element:", nums)

del nums[-1]
print("After deleting the last element:", nums)

nums.clear()
print("After clearing the entire list:", nums)

print("=====================")


user_list = []
n = int(input("Enter the number of elements you want in the list: "))
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

print("Original list:", user_list)

if len(user_list) > 0:
    del user_list[0]  
if len(user_list) > 0:
    del user_list[-1]  
print("After deleting the first and last elements:", user_list)

if len(user_list) > 3:
    removed_element = user_list.pop(3)
    print(f"Element removed at index 3: {removed_element}")
else:
    print("No element at index 3 to remove.")

print("Final list:", user_list)


print("=====================")

numbers = list(range(1, 11))
print("Original list:", numbers)

sublist = numbers[2:7]
print("Sublist (index 2 to 7):", sublist)

numbers.insert(5, 99)
print("List after inserting 99 after the fifth element:", numbers)


print("=====================")

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

sublist = my_list[1:4]
print("Extracted sublist:", sublist)


my_list[3] = 'x'
print("List after replacing 'd' with 'x':", my_list)


my_list.remove('g')  # remove 'g'
my_list.append('z')  # append 'z'
print("List after removing 'g' and appending 'z':", my_list)

