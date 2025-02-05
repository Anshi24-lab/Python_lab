print("===========START============")

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest


print(longest_palindrome("babad"))  


print("=======================")

def most_frequent_char(s):
    s = s.replace(" ", "").lower()
    max_char = max(s, key=s.count)
    return {'Character': max_char, 'Frequency': s.count(max_char)}


print(most_frequent_char("This is a test sentence"))


print("=======================")


def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result


print(compress_string("aaabbccca"))


print("=======================")

def find_anagrams(word, lst):
    word_sorted = sorted(word)
    return [w for w in lst if sorted(w) == word_sorted]


print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))


print("=======================")


def caesar_decode(cipher, shift):
    result = ""
    for char in cipher:
        if char.isalpha():
            shifted = chr((ord(char) - shift - 97) % 26 + 97)
            result += shifted
        else:
            result += char
    return result


print(caesar_decode("dwwdfn", 3))  


print("==========END=============")


