from pymongo import MongoClient
from prettytable import PrettyTable

MONGODB_URI = "mongodb+srv://adhyannegi:9975@cluster0.7ob2lez.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)

db = client["mydatabase"]
collection = db["GroceryStore"]


def add_item():
    ans = 'y'
    while ans in "Yy":
        name = input("Enter Name of Item: ")
        price = input("Enter Price in dollars: ")
        quantity = input("Enter Quantity in grams: ")
        rec = {"name": name, "price": price, "quantity": quantity}
        collection.insert_one(rec)
        print("Item added.")
        ans = input("Enter more data Y/N:")


def delete_item(name):
    result = collection.delete_one({"name": name})
    if result.acknowledged:
        if result.deleted_count == 1:
            print("Item deleted.")
        else:
            print("Item not found.")
    else:
        print("Item not found.")


def update_price(name, new_price):
    result = collection.update_one(
        {"name": name}, {"$set": {"price": new_price}})
    if result.modified_count == 1:
        print("Price updated.")
    else:
        print("Item not found.")


def update_quantity(name, new_quantity):
    result = collection.update_one(
        {"name": name}, {"$set": {"quantity": new_quantity}})
    if result.modified_count == 1:
        print("Price updated.")
    else:
        print("Item not found.")


def display():
    table = PrettyTable()
    table.field_names = ["Name", "Price", "Quantity"]
    for rec in collection.find():
        name = rec.get("name", "")
        price = rec.get("price", "")
        quantity = rec.get("quantity", "")
        table.add_row([name, price, quantity])
    print(table)


print('Welcome to the Grocery Store.')
opt = 'y'
while opt in 'Yy':
    print('1. Add a record to file.')
    print('2. Delete a record from file.')
    print('3. Edit price of an item.')
    print('4. Edit quantity of an item.')
    print('5. Display all records')

    choice = int(input('Enter your choice:(1-5): '))
    if choice == 1:
        add_item()
    elif choice == 2:
        name_of_item = input('Enter name of item to be deleted: ')
        delete_item(name_of_item)
    elif choice == 3:
        name_of_item = input('Enter name of item: ')
        new_price = input('Enter new price: ')
        update_price(name_of_item, new_price)
    elif choice == 4:
        name_of_item = input('Enter name of item: ')
        new_quantity = input('Enter new quantity: ')
        update_quantity(name_of_item, new_quantity)
    elif choice == 5:
        display()

    else:
        print('Invalid Choice.')
    opt = input('Do you want to continue(Y/N): ')

else:
    print('Data stored.')


client.close()
