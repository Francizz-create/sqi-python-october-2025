# library = []

# def add_book():
#     tittle = input("Enter book title: ")
#     author = input("Enter author name ")
#     year = input("Enter year of publication: ")
#     isbn = input("Enter ISBN: ")

#     book = {
#         "title": tittle,
#         "author": author,
#         "year": year,
#         "isbn": isbn,
#         "available": True
#     }
    
#     library.append(book)
#     print("Book added successfully!\n")

# def view_books():
#     if not library:
#         print("Library is empty.\n")
#         return
    
#     print("\n ALL BOOKS ")
#     for book in library:
#         status = "Available" if book["available"] else "Borrowed"
#         print(f"Title: {book["title"]}, Author: {book["author"]}, Year: {book["year"]}, ISBN {book["isbn"]}, Status: {status}")
    
#     add_book()



    
#class Car:
   # def __init__(self, color: str, brand : str, model, year_manufactured: int, engine : str, no_of_doors: int,):

        #self.color = color
        #self.brand = brand
        #self.model = model
        #self.year_manufactured = year_manufactured
#         #self.engine = engine
#         self.no_of_doors = no_of_doors
        
#     def move(self):
#         return "Car is moving"
    
#     def reverse(self):
#   #      return "Car can reverse"
    
# #    def honk(self):
#  #       return "car can honk"

#     def car_spec(self):
  #      return f"This is a {self.year_manufactured} {self.model} {self.brand} car, with {self.color} color, {self.engine} engine, {self.no_of_doors} doors,"

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

class ShoppingCart:
    def __init__(self, owner, items:dict[str,int]):
        self.owner = owner
        self.items = items

    def add_item(self, item, price):
        self.items[item] = price
    def total_cost(self):

        