# Project Overview:
# Create a simple phone book manager where users can add, view, update, and delete contacts
# in a file named `phone_book.py`.

# 1.Requirements:
# Data Storage: Use a list of dictionaries to store contact information. Each contact should have the following attributes:
# Name (string)
# Phone Number (string)
# Favorite (boolean)

# 2.Functions/Actions:
# add_contact(): Add a new contact to the phone book.
# view_contacts(): Display all the contacts in the phone book.
# update_contact(phone_number): Update the information of a contact given their phone number.
# delete_contact(phone_number): Remove a contact from the phone book using their phone
# number.

# 3.search_contact(name): Search for a contact by their exact name.
# mark_favorite(phone_number): Mark a contact as a favorite.
# unmark_favorite(phone_number): Unmark a contact as a favorite.
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit.
#  Assume the user always inputs the correct data types.


phone_book = []
    
def add_contact(name:str, phone_number: str, favorite=False):
    contact = {
        "name": name,
        "phone_no": phone_book,
        "favorite":favorite
    }
    phone_book.append(contact)
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not phone_book:
        print("Phone book is empty.")
    else:
        for contact in phone_book:
            fav_status = "⭐" if contact["favorite"] else ""
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']} {fav_status}")

def update_contact(phone_number, new_name=None, new_number=None):
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            if new_name:
                contact["name"] = new_name
            if new_number:
                contact["phone_number"] = new_number
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(phone_number):
    for contact in phone_book:
        if contact["phone_number"] == phone_number:
            phone_book.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def search_contact(name):
    for contact in phone_book:
        if contact["name"].lower() == name.lower():
            fav_status = "⭐" if contact["favorite"] else ""
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone_number']} {fav_status}")
            return
    print("Contact not found.")


    