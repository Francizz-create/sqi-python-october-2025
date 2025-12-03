

# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]

digits = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in digits]
print(squares)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]

names = ["John", "Sara", "Mike", "Amanda"]

names_with_a = [name for name in names if "a" in name.lower()]
print(names_with_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]


values = [5, 12, 3, 18, 7]

greater_num = [num > 10 for num in values]
print(greater_num)


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]


animals = ["dog", "cat", "lion", "tiger"]

last_chars = [word[-1] for word in animals]
print(last_chars)

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False

values = [5, 12, 3, 18, 7]

result = all(num > 10 for num in values)
print(result)


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True

names = ["John", "Sara", "Mike", "Amanda"]

result = any("a" in name.lower() for name in names)
print(result)

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False

greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

result = all(word.isupper() for word in greetings)
print(result)

# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True

words = ["apple", "zebra", "mango", "lemon"]

result = any(word.lower().startswith("z") for word in words)
print(result)

# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True

emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

any_org = any(".org" in email for email in emails)
print(any_org)


# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True

values = [1, 3, 5, 7, 9]

all_odd = all(num % 2 != 0 for num in values)
print(all_odd)

# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False

words = ["hi", "dog", "go", "sun"]

all_longer = all(len(word) > 2 for word in words)
print(all_longer)

# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]

nums = [2, 4, 6, 8]

tripled = [num* 3 for num in nums]
print(tripled)

# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False

temperatures = [12, 7, 3, -1, 5]

above_zero = all(temp > 0 for temp in temperatures)
print(above_zero)

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True

fruits = ["banana", "mango", "kiwi", "grape"]
vowels = "aeiouAEIOU"

ends_with_vowel = [word[-1] in vowels for word in fruits]

print(ends_with_vowel)


# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]

greetings = ["HELLO", "WORLD", "PYTHON"]

lowercase = [word.lower() for word in greetings]
print(lowercase)

# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True


numbers = [5, 4, 3, 3, 8]

any_negative = any(num < 0 for num in numbers)
print(any_negative)

# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]

items = ["sky", "tree", "rock", "stone"]

words_with_e = [word for word in items if "e" in word]
print(words_with_e)

# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False

names = ["Alice", "Bob", "charlie", "David"]

all_upper = all(name[0].isupper() for name in names)
print(all_upper)

# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True

sentences = ["Short one", "This is a much longer sentence", "Okay"]

longer_than = any(len(word) > 20 for word in sentences)
print(longer_than)



password = input("Enter your password: ")
special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in special_characters for char in password)
long_enough = len(password) >= 8

is_strong = (has_upper, has_lower, has_digit, has_special, long_enough)

print(all(is_strong))