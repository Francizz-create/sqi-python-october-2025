# 1.Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
#  length, width, and height, and print each variable.
dimensions = (10, 20, 30)
length, width, height = dimensions
print(length)
print(width)
print(height)
 
# 2.Given the tuple coordinates:
#  coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.

coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(y) 
 
# 3.Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession,
#  and print the value of profession.

person = ("John", 25, "Engineer")
name, age, profession = person
print(profession)

# 4.Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.

data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
student1, student2 = data[0]
print(student2)

# 5.Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2,
#  and print both variables.

colors = ("red", "green", "blue", "yellow")
color1,color2,_,_ = colors
print(color1)
print(color2)
 
# 6.Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments.
# Print the extracted age and the first department.

record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, position),(first_dept, second_dept) = record
print(name)
print(age,position)
print(first_dept,second_dept)

# 7.Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.

triplet = ("one", "two", "three")
num1, num2, numm3 = triplet
print(num2)

# 8.Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.

info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
productID, (category, price), (day, month, year) = info
print(category)
print(year)

# 9.Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.

nested_tuple =(("a", "b"), ("c", "d"), ("e", "f"))
(a1, a2), (b1, b2), (c1, c2) = nested_tuple
print(c2)

# 1O.Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas# 

inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(fruit1, q1), (fruit2, q2), (fruit3, q3) = inventory
print(q2)

#>>>>>>>OR<<<<<<<<<
(_,_), (fruit2, qty2), (_,_) = inventory
print(qty2)