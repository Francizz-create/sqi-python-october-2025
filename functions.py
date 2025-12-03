# def my_name():
#     print("Olusegun Olaniyi Francis")

# my_name()

# def times(num):
#     print(num * 2)

# times(5)

# def greet(name):
#     print(f"I am {name}")

# greet("Francis")

# def raise_to_power(num, num2):
#     print(num ** num2)

# raise_to_power(2 ,3)


# def change_to_lower(word):
#     return word.lower()
# print(change_to_lower("FRANCIS"))

# def upper_everyone(names = []):
#     return [name.upper() for name in names]
# print(upper_everyone(["francis","david", "fatima", "chisom"])

# def starts_with_m(word):
#     return word.lower().startswith("m")
# print(starts_with_m("Maddie"))
# print(starts_with_m("john"))
# print(starts_with_m("marry"))

# def is_even(num):
#     return num % 2 == 0
# print(is_even(3))
# print(is_even(6))

# def is_alliteration(words: str):
#     two_word_string = words.lower().split()
#     return two_word_string[0][0] == two_word_string[1][0]
        

# print(is_alliteration("francis olusegun"))



# ====================================ASSIGNMENT===========================================


# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.

def get_total_length(*chars):
    total = 0
    for char in chars:
        total += len(char)
    return total


# Test Data:
print(get_total_length("apple", "banana", "car"))
print(get_total_length("hi", "hello"))

# Expected Output:
# 14
# 7


# 2. Create a function called highest_score that returns the name of the student with the highest score.


# Test Data:
# print(highest_score(Ada=72, Bisi=89, Charles=67))
# print(highest_score(Emeka=90, Tolu=91, Zainab=88))

# Expected Output:
# Bisi
# Tolu

# 3. Create a function called multiply_first_two that returns the product of the first two numbers passed in.

def multiply_first_two(*numbers):
    
    return numbers[0] * numbers[1]

# Test Data:
print(multiply_first_two(3, 5, 2, 9))
print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20


# 4. Create a function called describe_books that prints out each book title and its author.

def describe_books(**book_dict):
    for title, author in book_dict.items():
        print(f"{title} is written by {author}")

# Test Data:
describe_books(Hamlet ="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")

describe_books{Matilda="Roald Dahl", 1984 ="George Orwell"},l,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,lambda




# Expected Output:
# Hamlet is written by Shakespeare
# ThingsFallApart is written by Chinua Achebe
# Dune is written by Frank Herbert
# Matilda is written by Roald Dahl
# 1984 is written by George Orwell

# 5. Create a function called total_age that returns the sum of all the ages given.

def total_age(**ages):
    for age in ages:
        return 

# Test Data:
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# Expected Output:
# 60
# 65


# 6. Create a function called list_countries that prints out each country passed in.

# Test Data:
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# Expected Output:
# Nigeria
# Ghana
# Kenya
# Canada
# Mexico

# 7. Create a function called student_details that prints each student’s name and score.

# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.

# Test Data:
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# Expected Output:
# 2400
# 1700


# 10. Create a function called first_and_last that prints the first and last values passed in.

# Test Data:
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# Expected Output:
# First: 4, Last: 12
# First: a, Last: d

# 11. Create a function called describe_animals that prints out animal and their sound.

# Test Data:
# describe_animals(cat="meow", dog="bark", cow="moo")
# describe_animals(lion="roar", snake="hiss")

# Expected Output:
# cat makes the sound meow
# dog makes the sound bark
# cow makes the sound moo
# lion makes the sound roar
# snake makes the sound hiss


# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.

# Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 15
# 7


# 13. Create a function called find_minimum that returns the smallest number from all the values passed in.

# Test Data:
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))

# Expected Output:
# 12
# 3


# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150


# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration
