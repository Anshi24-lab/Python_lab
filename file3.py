# 1. Basic Indexing
text = "Python Programming"
print("First character:", text[0])
print("Last character:", text[-1])
print("7th character:", text[6])


print("=======================")


# 2. Slicing
print("Substring 'Python':", text[:6])
print("Substring 'Programming':", text[7:])
print("Every alternate character:", text[::2])
print("Reversed string:", text[::-1])


print("=======================")


# 3. Nested Indexing
nested_text = "Learn Python [Basics]"
print("Substring 'Basics':", nested_text[14:-1])
print("Substring '[Basics]':", nested_text[13:21])


print("=======================")


# 4. String Length
sentence = "Data Analytics using Python"
print("Length of the string:", len(sentence))


print("=======================")


# 5. Changing Case
print("Uppercase:", "hello world".upper())
print("Lowercase:", "PYTHON IS FUN".lower())
print("Capitalized:", "machine learning".capitalize())

print("=======================")


# 6. Finding and Replacing
quote = "The quick brown fox jumps over the lazy dog"
print("Index of 'fox':", quote.find("fox"))
print("Replaced string:", quote.replace("lazy dog", "active cat"))

print("=======================")


# 7. String Splitting and Joining
words = "apple,banana,cherry"
word_list = words.split(',')
print("List of words:", word_list)
joined_string = ' '.join(word_list)
print("Joined string:", joined_string)


print("=======================")


# 8. Checking Membership
membership_string = "Learn Python Programming"
print("Does 'Python' exist?:", "Python" in membership_string)
print("Starts with 'Learn' and ends with 'Programming':", 
      membership_string.startswith("Learn") and membership_string.endswith("Programming"))


print("=======================")


# 9. Whitespace Removal
messy_text = " Clean this text "
print("Without leading whitespace:", messy_text.lstrip())
print("Without trailing whitespace:", messy_text.rstrip())
print("Without leading and trailing whitespace:", messy_text.strip())


print("=======================")

# 10. Counting Substrings
paragraph = "Python is powerful. Python is versatile. Python is easy to learn."
print("Occurrences of 'Python':", paragraph.count("Python"))
print("Occurrences of 'i':", paragraph.count("i"))
