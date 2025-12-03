#my_favourite_fruits = ["Banana", "orange", "apple"]#

#print(my_favourite_fruits)#

#print()

#means_of_transport = ["car", "lorry", "camel", "ship", "canoe"]#

##Q1
#means_of_transport.append("plane")
#print(means_of_transport)#

##Q2 
#means_of_transport.insert(2,"jet")
#print(means_of_transport)#

##Q3
#print("helicopter" in means_of_transport) #

##Q4
#means_of_transport.remove("canoe")
#print(means_of_transport)#

##Q5
#means_of_transport[1]=  "van"
#print(means_of_transport)#

##Q6
#means_of_transport.extend(["helicopter","broom"])
#print(means_of_transport)


# =====================================================
# ASSIGNMENT— LISTS
# =====================================================

# 1. Print the second and second-to-last items in the list.
# Input: animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]
# Expected Output:
# cat
# sheep

#animals =  ["dog", "cat", "goat", "cow", "sheep", "horse"]
#print(animals[1])
#print(animals[-2])#
#

## 2. Replace the first and last items with "lion" and "elephant", then print the list.
## Input: animals = ["dog", "cat", "goat", "cow", "sheep", "horse"]#

#animals[0] = "Lion"
#animals[-1] = "elephant"
#print(animals)#

## 3. Add "pig" to the list and then insert "hen" at index 2.
## Input: animals = ["dog", "cat", "goat"]
#animals2 = ["dog", "cat", "goat"]
#animals2.append("pig")
#animals2.insert(2, "hen")
#print(animals2)#
#

## 4. Remove "cow" from the list and print the updated list.
## Input: animals = ["dog", "cat", "cow", "goat", "sheep"]
#animals3 = ["dog", "cat", "cow", "goat", "sheep"]
#animals3.remove("cow")
#print(animals3)#
#

## 5. Check if "goat" is in the list and print the result.
## Input: animals = ["dog", "cat", "cow", "goat", "sheep"]
#animals4 = ["dog", "cat", "cow", "goat", "sheep"]
#print("goat" in animals4)#
#

## 6. Combine two lists of foods and print the result.
## Input: list1 = ["rice", "beans"], list2 = ["yam", "plantain"]#

#list1 = ["rice", "beans"]
#list2 = ["yam", "plantain"]
#result = list1 + list2
#print(result)#
#

## 7. Create a list of drinks and check if "water" exists.
## Input: drinks = ["tea", "coffee", "juice", "soda"]
#drinks = ["tea", "coffee", "juice", "soda"]
#print("water" in drinks)#
#

## 8. Add "water" and "milk" at once to the list.
## Input: drinks = ["tea", "coffee", "juice"]
#drinks1 = ["tea", "coffee", "juice"]
#drinks1.extend(["water", "milk"])
#print(drinks1)#
#

## 9. Replace "coffee" with "hot chocolate" and print the list.
## Input: drinks = ["tea", "coffee", "juice"]
#drinks2 = ["tea", "coffee", "juice"]
#drinks2[1] = "hot chocolate"
#print(drinks2)#
#

## 10. Create a list of vehicles, add and remove some items step by step.
## Input: vehicles = ["car", "bike", "bus", "train"]#

## Steps:
##   1. Add "boat" to the end
##   2. Insert "truck" at index 1
##   3. Remove "bike"
##   4. Check if "plane" exists#

#vehicles = ["car", "bike", "bus", "train"]
##1
#vehicles.append("boat")
##2
#vehicles.insert(1, "truck")
##3
#vehicles.remove("bike")#

#print(vehicles)
##4
#print("plane" in vehicles)#
#

## 11. Append "Abuja" to the end of the list.
## Input: cities = ["Lagos", "Kano", "Ibadan"]
#cities = ["Lagos", "Kano", "Ibadan"]
#cities.append("Abuja")
#print(cities)#
#

## 12. Extend the list with another list of cities.
## Input: cities = ["Lagos", "Kano"], more_cities = ["Abuja", "Enugu"]
#cities = ["Lagos", "Kano"]
#more_cities = ["Abuja", "Enugu"]
#all_cities = cities + more_cities#

#print(all_cities)
#cities = ["Lagos", "Kano"]
#more_cities = ["Abuja", "Enugu"]
#all_cities = cities + more_cities#

#print(all_cities)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Assignment<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#1. Create a list called fruits with items "apple", "banana", and "orange". Print the first item.

fruits = ["apple", "banana", "orange"]
print(fruits[0])

#2. Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.

colors = ["red", "green", "blue"]
print(colors[-1])

#3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7 (inclusive of index 3, exclusive of 8).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

#4. Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabets[-3:])

#5. Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.

ages = [20, 30, 40]
ages[1]= 35
print(ages)

#6. Create a list called grades with items "A", "B", "C", "D". Replace the items from index 1 (inclusive) to index 3 (exclusive) with "X".

grades = ["A", "B", "C", "D"]
grades[1:3]= ["x"]
print(grades)

#7. Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.

cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)

#8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#9. Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.

prices = [10.5, 20.0, 15.75]
print(type(prices))

#10. Create a list called mixed with items 10, "apple", True. Print the list.

mixeed = [10, "apple", True]
print(mixeed)

#11. Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.

tuple_data = ("a", "b", "c")
lists = list(tuple_data)
print(lists)

#12. Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.

books = ["Python", "Java"]
books.append("Javascript")
print(books)

#13. Create a list called names with items "Alice", "Bob", "Eve" Insert "Charlie" at index 1.

names = ["Alice", "Bob", "Eve"]
names.insert(1,"charlie")
print(names)

#14. Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#15. Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.

students = ["Alice", "Bob"]
new_students = ("Charlie", "David") 
students.extend(new_students)
print(students)

#16. Create a list called colors with items "red", "green", "blue". Remove "green" from the list.

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

#17. Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.

numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

#18. Create a list called fruits with items "apple", "banana", "cherry". Clear the list.

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# 19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.

names = ["Zoe", "Alice", "Bob"]
names.sort()
print(names)

# 20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.

ages = [25, 35, 20]
ages.sort(reverse=True)
print(ages)

# 21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
#"Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.

words = ["Apple", "banana", "Orange"]
words.sort(key=str.lower)
print(words)

# 22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.

numbers = [1, 2, 3, 4]
numbers.sort(reverse = True)
print(numbers)

# 23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
#slicing.

letters = ["a", "b", "c", "d"]
print(letters[::-1])


# 24.	Create a list called original with items "one", "two", "three". Create a copy of the list.

original = ["one", "two", "three"]
copy_list = original.copy()
print("original", original)
print("copy", copy_list)

# 25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
#	list2 together.

list1 = ["a", "b"]
list2 = ["c", "d"]
list1.extend(list2)
print(list1)

# 26.	Access and print the second subject of the first person in the list.
#	data = [
#    ["Alice", 25, ["Math", "Physics"]],
#    ["Bob", 30, ["Chemistry", "Biology"]],
#    ["Charlie", 35, ["History", "Geography"]]

data =[
     ["Alice", 25, ["Math", "Physics"]],
     ["Bob", 30, ["Chemistry", "Biology"]],
     ["Charlie", 35, ["History", "Geography"]]
     ]
print(data[0][2][1])

# 27.	Access and print the first value in the list of numbers associated with "San Francisco".
#	records = [
#    ["New York", [10, 20, 30]],
#    ["San Francisco", [40, 50, 60]],
#    ["Austin", [70, 80, 90]]
#]

records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]

print(records[2][1])

# 28.	Get the first e in Ayo’s gender and Get Ben’s age.
# 	group = [
#    ["Ayo", ["Female", 12]],
#    ["Ben", ["Male", 9]]
#]

group = [
      ["Ayo", ["Female", 12]],
      ["Ben", ["Male", 9]]
]
print(group[0][1][0][1:2])
print(group[1][1][1])

# 29.	Get the l in Nina’s gender and Get Tobi’s age
#	records = [
#    ["Tobi", ["Male", [6]]],
#    ["Nina", ["Female", [7]]]
#]

records = [
    ["Tobi", ["Male", 6]],
    ["Nina", ["Female", 7]]
]
print(records[1][1][0][4:5])
print(records[0][1][1])


# 30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
#robot_grid = [
#    ["R2", ["battery", [98]]],
#    ["R5", ["status", "active"]],
#    ["X1", [["joint", "loose"], "error"]]


robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", ["joint", "loose"], "error"]
]

print(robot_grid[2][1][1][1:3])
print(robot_grid[0][1][1])

# 31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
#playlist = [
#    ["Jazz", ["Take Five", 5.24]],
#    ["Pop", ["Blinding Lights", 3.20]],
#    ["Rock", ["Bohemian Rhapsody", 5.55]]
#]


playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][1][0][5:])
print(playlist[0][1][1])


# 32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
#animals = [
#    ["Elephant", ["Herbivore"]],
#    ["Tiger", ["Carnivore"]],
#    ["Frog", ["Amphibian"]]

animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
print(animals[1][1][0][5:6])
print(animals[2][1][0][:1])

original = ["one", "two", "three"]
duplicate = original.copy()
#print(id(original))
print(duplicate)