 # native_soups = ("ewedu", "banga soup", "eforiro", "egusi", "oha")

# for soup in native_soups:
#     for char in soup:
#         print(char)

#     print("\n")



# native_soups = {"ewedu": "yoruba",  "banga soup": "igbo", "eforiro": "edo", "egusi": "hausa"}

# for soup, tribe in native_soups.items():
#     print(f"The tribe that eats {soup} is {tribe}")


# native_soups = ("ewedu", "banga soup", "eforiro", "egusi", "oha")

# for soup in native_soups:
#     if soup == "egusi":
#         continue
#     print(soup)
# print()
# print()
# print()

# for soup in native_soups:
#     if soup == "banga soup":
#         break
#     print(soup)

# dog_breeds = ["Rotweiller", "Chihuahua", "Poodle", "Doberman", "Pitbull", "Lhasa Apso", "Boer boel", "Ekuke"]

# for i in range(len(dog_breeds)):
#     print(f"The breed {i+1} is {dog_breeds[i]}")

#  6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# num = int(input("Enter the numbeer: "))
#
# a,b = 0, 1
# for i in range(num):
#     print(a, end=",")
#     a, b = b, a + b

#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

num = input("Enter some numbers: ")
num_list = num.split(",")
for i in range(len(num)):
     num_list = int(num_list[i])
largest = num_list[0]

for num in num_list:
     if num > largest:
          largest = num
print("The largest number is:", largest)
        

#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# # 	Output: 30 (2 + 4 + 6 + 8 + 10)

# num = int(input("Enter an integer: "))

# for numbers in range(2,num +2, 2):
#     print(f"\n ")

#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

#  10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)
#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"
#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4
#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence
#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.
#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.
#  16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of
#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.
#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B


#  19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

#  20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
