# i = 40
# while i <= 76:
#   print(i)
#   i+=1#


# i = 56
# while i >= 12:
#   if i % 2 == 0:
#        print(i)
#   i -= 2

# i = 1
# numbers = []
# while i <= 50:
#    numbers.append(i)
#    i += 1
# print(numbers)

# name = input("Enter your name: ")
# i = 1
# while i <= len(name):
#    print(f"hello, {name}")
#    i += 1

# i = 60
# numbers = []
# while i <= 100:
#    numbers.append(i)
#    if i == 69:
#        break
#    i += 1
# print(numbers)#


# i = 9
# numbers = []
# while i <= 19:
#    i += 1
#    if i == 15:
#        continue
#    numbers.append(i)
# print(numbers)

# n = int(input("Enter the number: "))
# total = 0
# num = []
# i = 1
# while i <= n:
#    num.append(str(i))
#    total += i
#    i += 1
# print(f"{num}")# 

# lenght = int(input("Enter the length: "))
# i = lenght
# num = []
# num.append(i)
# while i == num:



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# # 1.Print numbers from 1 to 5# 

# i = 1
# while i <= 5:
#     print(i)
#     i += 1# 
# 

# # 2.Print "Hello" 3 times# 

# i = 1
# while i <= 3:
#     print("Hello")
#     i += 1# 

# # 3.Print only even numbers from 2 to 10 (do not use += 2)# 

# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1# 

# # 4.Print numbers in reverse from 5 to 1 using a while loop.# 

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1# 

# #  5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. # 

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1# 
# 

# #  6. 	Print a square of stars
# # Ask the user to enter a number
# # Example 1:
# # Input: 3# # 

# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print("*" * n)
#     i += 1# 

# #  7.	Print a right triangle of stars
# # Ask the user to enter a number# 

# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print("*" * i)
#     i += 1# 
# 

# #  8. 	Print a countdown
# # Ask the user to enter a number where they want to start the countdown from.# 

# n = int(input("Enter a number to start countdown: "))
# while n > 0:
#     print(n)
#     n-= 1 
# print("Go!")# 

# # Go!
# #  9. 	Print "1" ten times on the same line using a while loop# 

# i = 0
# while i < 10:
#     print("1", end="")
#     i += 1# 
# 

# # 10.  Print a list of the first 12 multiples of 3 starting from # 



# # >>>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<<<<# 

# # 1.Write a program that uses a while loop to print numbers from 1 to 10.# 

# i = 1
# while i <= 10:
#     print(i)
#     i += 1# 

# # 2.Write a program that takes an integer n from the user and calculates the sum of all 
# # natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).# 

# n  = int(input("Enter a number: "))
# i = 1
# total = 0# 

# while i <= n:
#     total += i
#     i += 1
# print("The sum of natural numbers up to", n, " is", total)# # 

# # 5.Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.# 

# n  = int(input("Enter a number to start countdown: "))
# while n >= 0:
#     print(n)
#     n -= 1# 
# 

# # 6.Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.# 

# n  = int(input("Enter an integer: "))
# while n > 0:
#     print(n)
#     n -= 1# 
# 

# # 7.Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.# 

# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# result = 1
# i = 0# 

# while i < exponent:
#     result *= base
#     i +=1
# print(f"{base} raised to the power of {exponent} is {result}")

# 

# sentence = input("Enter a sentece: ")
# i = 0
# while i < len(sentence):
#     print(sentence[i])
#     i += 1# 

# musical_instruments = ["gong", "drum", "saxophone", "guitar", "keyboard"]# 

# i = 0
# while i < len(musical_instruments):
#     print(f"{i + 1}",  musical_instruments[i])
#     i += 1# 

# food = input("Enter your favourite food: ")
# while food.startswith("r"):
#     print(f"done")
#     break
# else:
#     print("food must start with R")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<

# 1. Write a program that uses a while loop to print numbers from 1 to 10.


# 2. Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).


# 3. Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. 
# E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.


# 4. Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# correct_password = "secret"
# password = ""
# while password != correct_password:
#     password = input("Enter password: ")
#     if password != correct_password:
#         print("Wrong passworrd, try again")
# print("Access granted")



# 9. Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().# 


# 8. Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# text = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# i = 0

# while i < len(text):
#     char = text[i]
#     if char in vowels:
#         count += 1
#     i += 1


# 10.	Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#       Use the min() function.

#  11. 	Write a program that takes a string input from the user and uses a while loop to count
# 	the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# text = input("Enter a string: ")
# char_count = {}
# i = 0# 

# while i < len(text):
#     char = text[i]
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#     i += 1
# print(char_count)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop.
#  The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# total = 0
# while True:
#     price = float(input("Enter the price of the item: "))
#     total += price

#     choice = input("Do you want to add another item (yes/no): ")
#     if choice != "yes":
#         break
# print(f"\nTotal cost of items: {total:}")



# 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.# 

# while True:
#     password = input("Enter your password: ")

#     if len(password) >= 8 and len(password) <= 25:
#         print("password accepted.")
#         break
        
#     else:
#         print("Invalid password! password must be between 8 and  25 characters long.\n")




#  4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.
    
# while True:
#     age = (input("Enter your age: "))
    
#     if age.isnumeric():
#         age = int(age)
#         if age >= 0:
#             print("Age accepted")
#             break
#         else:
#             print("Invalid age. Please enter a valid age.")
#     else:
#         print("Invalid input, must be number")


#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}

# iventory = {
# "eggs": 40,
# "fish": 200,
# "bread": 343,
# 'yam': 2
# }

# 
# Current iventory:", iventory)
# Options:")
#  Add item")
#  Remove item")
#  Exit")
# 
# input("Enter your choice (1/2/3):")
# 
#  == "1":
# = input("Enter item name to add: ").lower
# ity = int(input("Enter quantity: "))
# em in iventory:
# ventory[item] += quantity
# 


# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

# 




# >>>>>>>>>>>>>>>>>>>>>ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# 1.Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)

# num = int(input("Enter a numbers: "))
# total = 0
# while num > 0:
#     digit =  num % 10
#     total += digit
#     num //= 10
# print("sum of digits:", total)


# 2.Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

text = input("Enter a string: ").strip().lower()
i = 0
vowels = 0
consonants = 0
while i < len(text):
    char = text[i]
    if char in "aeiou":
        vowels += 1
    else:
        consonants += 1
    i += 1
print("vowels", vowels, "consonants", consonants)


# 3.Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

i = 0
num = int(input("Enter a number: "))

while i < 12:
    i += 1
    print(num, "x", i, "=", num * i)


# 4.Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

text = input("Enter some text: ")
i = len(text) - 1
reversed_text = ""

while i >= 0:
    reversed_text += text[i]
    i -= 1

print(reversed_text)



# 5.Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]



