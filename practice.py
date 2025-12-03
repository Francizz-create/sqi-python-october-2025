# my_list = []
# re_my_list = my_list[::-1]
# print(re_my_list)

# original_list = ["food", "drugs", "money", "savings"]
# reversed_list = original_list[::-1]
# reversed_list.sort(reverse=True)
# print("Reversed List:", reversed_list)

# tuple_list = ( 1,2,3,4,5)
# tuple_list = list(tuple_list)
# print(tuple_list)

# names = ["Alice", "Bob", "Eve"]
# names.insert(1, "charlie")
# print(names)
# umbers = [10, 20, 30, 40]
# del umbers[2]
# print(umbers)
# names = ["Zoe", "Alice", "bob"]
# names.sort(key=str.lower)
# print(names)


# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]

# print(data[0][2][1])
# a = 56
# b = 100
# if b > a:
#     print("b is greater than a")
# a = 25
# b = 23
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("b is not greater")
# a = 2
# b = 330
# print("A") if a > b else print("B")


# a = 330
# b = 330

# if a > b:
#     print("A") 
# elif a == b :
#     print("=")
# else:
#      print("b") 


# print("A") if a > b else print("=") if a == b else print("B")

x = 42

# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# print("Above ten,") if x > 10 else print("and also above 20!") if x > 20 else print("but not above 20.") # this will print only one result.

# Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# if a  > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")

# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, 
# "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x,y,z = input("Enter three numbers seperated by commas: ").strip(",")
# x,y,z = int(x),int(y),int(z)

# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("decreasing order")
# else:
    # print("neither")

    # Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.

# height = int(input("Enter height: "))
# with_adult = input("Are you with adult (yes/no): ")

# if height >= 120:
#     print("allowed")
# else:
#     if  with_adult == "yes":
#         print("allowed")
#     else:
#         print("not allowed")

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("no longer true")

# cities = ["New York", "Paris", "Tokyo", "Sydney", "Cairo"]
# for city in cities:
#     print(f"City: {city}")

# my_string = "Python is fun!"
# for char in my_string:
#     print(f"Character: {char}")

# i = 0
# while i <= 3:
#     print("hello")
#     i += 1

# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# i = 1
# while i <= 9:
#     i += 1
#     if i != 5:
#         print(i)

# num = int(input("Enter the number: "))
# i = 0
# while i <= num:
#     print("*" * num)
#     i += 1

# num = int(input("Enter the number: "))
# i = 1
# while i <= num:
#     print("*" * i)
#     i += 1
    
num = int(input("Enter the number: "))

while num >= 0:
    print(num)
    num -= 1
print("go")
