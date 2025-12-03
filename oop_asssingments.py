# # Fill in the Line class methods to accept coordinates as a pair of tuples and 
# # return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


class Line:
    def __init__(self, coor1, coor2): 
         self.coor1 = coor1
         self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5  # formula for distance = square root of (x2 - x1)**2 + (y2 - y1)**2

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)  # formula for slope (y2 - y1) / (x2 - x1)

# # EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6


# # Q2
# # Fill in the class

import math

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
       
    def volume (self):
         return round(math.pi * (self.radius ** 2) * self.height, 2)

    def surface_area(self):
        return round((2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2)), 2)

# # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2


#<<<<<<<<<<<<<<<<<<<<<BANK ACCOUNT>>>>>>>>>>>>>>>>>>>>>>

# Scenario: You want to create a bank account that supports deposits and withdrawals.

# Task: Create a bank account class that has two attributes:

# owner
# balance

# and two methods:
# deposit
# Withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values for the amounts into 
# the methods directly, no need for loops either.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"Deposit of: ${amount} accepted \nAvailable balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of :${amount} Accepted \nCurrent balance: ${self.balance}")
        else:
            print(f"Funds unavailable")

        

    

#1. Instantiate the class
acct1 = Account('Winnie', 100)

#2. Print the object
print(acct1)
# Output:
# Account owner: Winnie
# Account balance: $100

#3. Show the account owner attribute
print(acct1.owner)  # Winnie

#4. Show the account balance attribute 
print(acct1.balance)  # 100

#5. Make a series of deposits and withdrawals 
acct1.deposit(50)  # Output: Deposit Accepted

acct1.withdraw(15)  # Output: Withdrawal Accepted

#6. Make a withdrawal that exceeds the available balance 
acct1.withdraw(500)  # Output: Funds Unavailable


#<<<<<<<<<<<<<<<<<<<<SPACE MISSION>>>>>>>>>>>>>>>>>>>>>>>>>

class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel
        
    def launch(self):
        if self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name}!")
        else:
            print(f"Not enough fuel to launch.")

    def refuel(self,amount):
        if amount >= 0:
            self.fuel += amount
            print(f"{self.name} refueled by {amount}. Current fuel: {self.fuel}")
        else:
            print("Refuel amount must be positive.")
    
class CargoShip(Spacecraft):
    def __init__(self, name, fuel, cargo_weight: int):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def launch(self):
        fuel_needed = 50 + (self.cargo_weight*2)
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"Launching {self.name} with cargo! Fuel used: {fuel_needed}")
        else:
            print("Not enough fuel to launch with cargo.")

class PassengerShip(Spacecraft):
    def __init__(self, name, fuel, passenger_count: int):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count
    
    def launch(self):
       if self.passenger_count > 100:
            print(f"Too many passengers. Cannot launch.")
       elif self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name} with passengers!")
       else:
            print("Not enough fuel to launch.")

# SAMPLE EXECUTION
# Create objects
cargo_ship = CargoShip("Galactic Hauler", 200, 30)
passenger_ship = PassengerShip("Star Voyager", 100, 80)

# Attempt to launch both ships
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 200 - (50 + 30*2) = 90

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 100 - 50 = 50

# Refuel both ships
cargo_ship.refuel(50)
# Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

passenger_ship.refuel(30)
# Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# Launch again after refueling
cargo_ship.launch()
# Output: Launching Galactic Hauler with cargo!
# Fuel after launch: 140 - (50 + 30*2) = 30

passenger_ship.launch()
# Output: Launching Star Voyager!
# Fuel after launch: 80 - 50 = 30

# Try to refuel with invalid amount
cargo_ship.refuel(-10)
# Output: Cannot refuel with negative amount.

# Test PassengerShip with too many passengers
passenger_ship.passenger_count = 120
passenger_ship.launch()
# Output: Too many passengers. Cannot launch.

# Try to launch cargo ship with low fuel
cargo_ship.launch()
# Output: Not enough fuel to launch.

