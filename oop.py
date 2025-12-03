
# class Movie:
#     def __init__(self, title: str, producer: str, rating: int,):

#         self.title = title
#         self.producer = producer
#         self.rating = rating
    
#     def movie_type(self):
#         return f"The title of the movie is {self.title} rated PG {self.rating}, and produced by {self.producer}"

# movie1 = Movie("Peaky Blinders", "Thomas Shelby", 16)
        
# print(movie1.title)
# movie1.title = "Joe Alan"

# print(movie1.title)
# print(movie1.movie_type())


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ASSIGNMENT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# -----------------------------------------ASSIGNMENT-----------------------------------------------
# 1. Create a class called Book with the following attributes:
#    - title
#    - author
#    - genre
#    - page_count
#    - year_published
#
#    The class should have a method called short_description() that returns:
#    "{title} by {author} ({year_published}), {genre}, {page_count} pages."
#
#    After defining the class, create 3 different Book objects with different values.


# class Book: 
#     def __init__(self, title,author,genre,page_count,year_published):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.page_count = page_count
#         self.year_published = year_published

#     def description(self):
#         return f"{self.title} by {self.author} {self.year_published}, {self.genre}, {self.page_count} pages."
    
# book1 = Book("Atomic Habits", "James", "Self-help", 320, 2018)
# book2 = Book("1984", "George Orwell", "Dystopian", 300, 1949)
# book3 = Book("The color purple", "Alice Walker", "Fiction", 250, 1982)

# print(book1.description())
# print(book2.description())
# print(book3.description())
        


#-
# 2. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
# #    After defining the class, create 3 different Car objects with different values.


# class Car:
#     def __init__(self, brand, model, year, horsepower,  fuel_type):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type

#     def car_info(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}."

# car1 = Car("Tesla", "Model 3", 2022, 283, "Electric")
# car2 = Car("Mercedes Benz", "Gle 450", 2020, 362, "Petrol")
# car3 = Car("Lexus", "Rx 350", 2025, 275, "Petrol")

# print(car1.car_info())
# print(car2.car_info())
# print(car3.car_info())
        

# 3. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.


# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def avr_grades(self):
#         return sum(self.grades) / len(self.grades)
    
#     def is_passing(self):
#         return self.avr_grades() >= 50        

# # Example usage:
# s1 = Student("Alice", 20, [60, 75, 80, 90])
# s2 = Student("Bob", 19, [30, 40, 20, 45])

# print(s1.name, "average:", s1.avr_grades(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.avr_grades(), "passing:", s2.is_passing())

# Expected Output:
# Alice average: 76.25 passing: True
# Bob average: 33.75 passing: False


# 4. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.

# class Playlist:
#     def __init__(self,name, songs: list[str]):
#         self.name = name
#         self.songs = songs

#     def add_song(self, song):
#         self.songs.append(song)
        
#     def total_songs(self):
#         return len(self.songs)
    
#     def show_songs(self):
#         return ",".join(self.songs)

# # Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us


# 5. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.

# class ShoppingCart:
#     def __init__(self, owner, items: dict[str,int]):
#         self.owner = owner
#         self.items = items

#     def add_item(self,item, price):
#         self.items[item] = price

#     def total_cost(self):
#         return sum(self.items.values())
    
#     def most_expensive(self):
#         return max(self.items, key=self.items.get) 
        

# # Example usage:
# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())

# Expected Output:
# Total cost: 1625
# Most expensive item: Laptop
# ---------------------------------------------------------------------------------------------------



# class CartItem:
#     def __init__(self,item: str, price: int, no_of_items: int):
#         self.item = item
#         self.price = price
#         self.no_of_items = no_of_items

# class Cart:
#     def __init__(self,carts: list[CartItem]):
#         self.carts = carts

#     def  total(self):
#         return sum(cart.price * cart.no_of_items for cart in self.carts)

        

# cart_item1 = CartItem("Egga", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)

# print(Cart.total())


# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })

# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])




class Vehicle:
    def __init__(self, name: str):
        self.name = name
        
    def describe(self):
        return f"vehicle {self.name}"

class Car(Vehicle):
    def __init__(self, name, number_of_doors):
        super().__init__(name)
        self.number_of_doors = number_of_doors
    def describe(self):
        return f"Car: {self.name} with {self.number_of_doors}"
    

vehicle = Vehicle(name="Bicycle")
print(vehicle.describe())

car = Car(name="Toyota", number_of_doors=4)
print(car.describe())

# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# class Line:
#     def __init__(self, coor1, coor2): 
#         pass

#     def distance(self):
#         pass

#     def slope(self):
#         pass

# # EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6
