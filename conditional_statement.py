##number = int(input("Enter a number: "))
##is_even = number % 2 == 0
##if is_even:
##    print(f"it is even")
##else:
##    print(f"it is odd")##

##name = input("enter your name: ")
##if name.lower().startswith("a"):
##    print(f"Your name starts with A")
##else:
##    print(f"your name does not start with A")#

##grade = int(input("Enter your grade: "))
##if grade < 0:
##    print("invalid score")
##elif grade == 0 or grade <= 40:
##    print("your grade is F")
##elif grade >= 40 and grade <= 45:
##    print("your grade is E")
##elif grade >= 46 and grade <= 50:
##    print("your garde is D")
##elif grade >= 50 and grade <= 59:
##    print("your grade is C ")
##elif grade >= 60 and grade <= 69:
##    print("your name is B")
##elif grade >= 70 and grade <= 100:
##    print("your grade is A")
##elif grade > 100:
##    print("invalid score")#
#

##has_raincoat = False
##has_umbrella = False##

##if has_raincoat and has_umbrella:
##    print("You have double protection from the rain")
##elif has_raincoat or has_umbrella:
##    print("You are protected from the rain")
##else:
##    print("Yoiu are NOT protected from the rain")#

##You have a variable `mode`supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated"
## if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".#

##mode = input("enter the mode: ").lower()##

##if mode == "manual":
##    print("Manual mode activated") 
##elif mode == "automatic":
##    print("Automatic mode activated")
##elif mode == "off":
##    print("System is off")
##else:
##    print("mode is invalid")#

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

## Exercise 1
## An amusement park ride has these rules:
## - Must be at least 120 cm tall to ride.
## - If under 120 cm but with an adult, still allowed.
## - Otherwise, not allowed.#
#

#height = int(input("Enter height: "))
#with_adult = input("with adult? ")#

#if height >= 120:
#    print("Output: Allowed")
#else:
#    if with_adult == "yes":
#        print("Output: Allowed")
#    else:
#        print("Output Not Allowed")#
#

## Exercise 2
## An exam grading system with retake rule:
## The user enters exam score and retake status ("yes" or "no").
## - If score is at least 50, print "Pass".
## - If score is less than 50 but retake is "yes", print "Retake allowed".
## - If score is less than 50 and no retake, print "Fail".#
#

#score = int(input("What is your score: "))
#retake = input("Do you want to retake the exam? ")##

#if score >= 50:
#    print("pass")
#else:
#    if retake == "yes":
#        print("Retake Allowed")
#    else:
#       print("Fail")#
#

## Exercise 3
## A ride-hailing app calculates trip approval:
## The user enters distance (km) and wallet balance.
## Each km costs 200 units.
## - If wallet balance is enough for the trip, print "Trip confirmed".
## - If balance is less but at least half the cost, print "Add funds".
## - If less than half, print "Trip denied".#
#

#distance = int(input("Enter The Distance (in km): "))
#wallet_ballance = int(input("Enter Your Wallet Ballance: "))
#cost = distance * 200#

#if wallet_ballance >= cost:
#    print("Trip confirmed.")#

#elif wallet_ballance >= cost / 2:
#    print("Funds insufficient. Add funds.")
#else:
#    print("Trip denied")#
#
#
#

## Exercise 4
## An airport boarding system:
## The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
## - If both are "yes", print "Proceed to boarding".
## - If boarding pass is missing, print "No boarding pass".
## - If passport is missing, print "No passport".
## - If both missing, print "Denied entry".#
#

#boarding_pass = input("Do you have a boarding pass? (yes/no): ").lower()
#passport = input("Do you have your passport? (yes/no): ").lower()#

#if boarding_pass == "yes" and passport == "yes":
#    print("Proceed to boarding")
#elif boarding_pass == "no" and passport == "no":
#    print("Denied entry")
#elif boarding_pass == "no":
#    print("No boardning pass")
#elif passport == "no":
#    print("No passport")#

##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TASK 2<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

## 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
## statement that prints "a and b are both positive" if both a and b are positive, prints 
## "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
## neither is positive.#

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))#

#if a > 0 and b > 0:
#    print("Both are positive")
#elif a > 0 or b > 0:
#    print("Only one is positve")
#else:
#    print("Neither is positive")#

## 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order"
## if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.#

#x,y,z = input("Enter 3 numbers separated by commaas: ").split(",")
#x,y,z = int(x), int(y), int(z)
#if x < y < z:
#    print("Increasing order")
#elif x > y > z:
#    print("Decreasing order")#
#

## 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" 
## if it is, otherwise print "Not a palindrome".#

#palindrome = input("Enter a string:  ")#

#if palindrome == palindrome[::-1]:
#    print("Is a palindrome")
#else:
#    print("Not a palindrome")#

## 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal 
## and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.#

#x = int(input("Enter x: "))
#y = int(input("Enter y: "))
#z = int(input("Enter z: "))#

##x = (input("Enter x: ")).strip()
##y = (input("Enter y: ")).strip()    #best way
##z = (input("Enter z: ")).strip()#

#if x == y == z:
#    print("All are equal")
#elif x == y or y == z or x == z:
#    print("Two are equal")
#else:
#    print("All different")#

## 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check 
## if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0.
##  Otherwise, print "Invalid triangle".#

#angle1 = int(input("Enter first angle: "))
#angle2 = int(input("Enter second angle: "))
#angle3 = int(input("Enter third angle: "))#

##if angle1 + angle2 + angle3 == 180 and #

## 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u,
##  both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.#

#ch = input("Enter a single character: ").strip().lower()#

#if ch in "aeiou":
#    print("Vowel")
#elif ch.isalpha():
#    print("Consonant")
#else:
#    print("Not a letter")#

## 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors
##  are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".#

#color1 = input("Enteer first color: ").lower()
#color2 = input("Enteer second color: ").lower()
#color3 = input("Enteer third color: ").lower()


# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints 
# "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".


 
# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", 
# "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message"



# 10.	You have two variables, status1 and status2, provided through user input, each of 
#	which can be "active", “inactive", or "pending". Write an if statement to print 
#	"Both active" if both statuses are "active", "One active" if exactly one is "active",
#	and "None active" if neither is "active".

status_one = input("Enter first status: ").strip().lower()
status2 = input("Enter second status: ").strip().lower()
if status_one == "active" and status2 == "active":
    print("Both active")
elif status_one == "active" or status2 == "active":
    print("One is active")
else:
    print("None active")

# 11. 	Given a string `filename` supplied by the user, write an if statement to check if the
#	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
#	print "Not an image file".

filename = input("Enter filename: ").strip().lower()
if filename.endswith((".jpg", ".png", ".gif")):
    print("Image file")
else:
    print("Not an image file")


# 12. 	You have a variable `access_level` provided through user input which can be "admin",
#	"user", or "guest". Write an if statement that prints "Full access" if access_level is
#	"admin", "Limited access" if it is "user", and "No access" if it is "guest".

access_level = input("Enter access level: ").strip().lower()

if access_level == "admin":
    print("Full access")
elif access_level == "user":
    print("Limited access")
elif access_level == "guest":
    print("No access")
else:
    print("Invalid access level")

# 13. 	Given a string `email` collected from the user, write an if statement to check if the
#	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
#	print "Invalid email".

email = input("Emter email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# 14. 	You have a variable `day` provided by user input which can be any day of the week 
#	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
#	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

day = input("Enter day of the week: ").capitalize()
if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")

# 15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
#	input from the user and prints the greatest number. Use conditional statements
#	to determine which number is the greatest. Bonus point if you can do it without `else` 
#	staments.
num1, num2, num3 = input("Enter three numbers: ")

if num1 >= num2:
    print(f"{num1} is the greatest")
