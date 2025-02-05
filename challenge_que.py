# Check if the string "madam" is a palindrome
string = "madam"
is_palindrome = string == string[::-1]
print(f"Is '{string}' a palindrome?: {is_palindrome}")

print("=======================")

# Check if "listen" and "silent" are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
print(f"Are '{str1}' and '{str2}' anagrams?: {are_anagrams(str1, str2)}")

print("=======================")

# Count the number of times each word appears in the sentence
sentence = "the quick brown fox jumps over the lazy dog"
word_list = sentence.split()
word_frequency = {word: word_list.count(word) for word in word_list}
print("Word frequencies:", word_frequency)


print("=======================")

# Extract digits and alphabetic characters from a mixed string
import re

mixed_string = "Python3.8 is awesome!"
digits = ''.join(re.findall(r'\d|\.', mixed_string))
letters = ''.join(re.findall(r'[a-zA-Z]', mixed_string))
print("Extracted digits:", digits)
print("Extracted letters:", letters)


print("=======================")

# Remove all special characters from a string
special_text = "Hello@$%& World!!!"
cleaned_text = ''.join(char for char in special_text if char.isalnum() or char.isspace())
print("String after removing special characters:", cleaned_text)
